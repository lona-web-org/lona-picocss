async def test_screenshots(lona_app_context):
    from lona_picocss.html import HTML, H1, InlineButton
    from lona_picocss import install_picocss, settings
    from lona import View

    from playwright.async_api import async_playwright

    def setup_app(app):
        install_picocss(app=app, debug=True)

        @app.route('/')
        class HelloWorldView(View):
            def handle_button_click(self, input_event):
                self.button.set_text('I was clicked')

            def handle_request(self, request):
                self.button = InlineButton(
                    'Click Me',
                    handle_click=self.handle_button_click,
                )

                return HTML(
                    H1('Hello World'),
                    self.button,
                )

    context = await lona_app_context(setup_app)
    settings_loaded_selector = '#lona h1:has-text("Pico.css Settings")'

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch()
        browser_context = await browser.new_context()
        page = await browser_context.new_page()

        # it works
        await page.goto(context.make_url('/_picocss/it-works'))
        await page.wait_for_selector('#lona h1:has-text("It works!")')
        await page.screenshot(path='doc/screenshots/it-works.png')

        # hello world
        await page.goto(context.make_url('/'))
        await page.wait_for_selector('#lona h1:has-text("Hello World")')
        await page.screenshot(path='doc/screenshots/hello-world.png')

        # settings
        await page.goto(context.make_url('/_picocss/settings'))
        await page.wait_for_selector(settings_loaded_selector)
        await page.screenshot(path='doc/screenshots/settings.png')

        # error pages #########################################################
        # 403
        await page.goto(context.make_url('/_picocss/forbidden-error'))
        await page.wait_for_selector('#lona h1:has-text("Error 403")')
        await page.screenshot(path='doc/screenshots/error-403.png')

        # 404
        await page.goto(context.make_url('/_picocss/not-found'))
        await page.wait_for_selector('#lona h1:has-text("Error 404")')
        await page.screenshot(path='doc/screenshots/error-404.png')

        # 500
        await page.goto(context.make_url('/_picocss/internal-error'))
        await page.wait_for_selector('#lona h1:has-text("Error 500")')
        await page.screenshot(path='doc/screenshots/error-500.png')

        # components ##########################################################
        # icons
        await page.goto(context.make_url('/_picocss/components/icons?no-form'))
        await page.wait_for_selector('#lona h1:has-text("Icons")')
        await page.screenshot(path='doc/screenshots/icons.png')

        # cards
        await page.goto(context.make_url('/_picocss/components/cards'))
        await page.wait_for_selector('#lona h1:has-text("Cards")')
        await page.screenshot(path='doc/screenshots/cards.png')

        # forms
        await page.goto(context.make_url('/_picocss/components/forms'))
        await page.wait_for_selector('#lona h1:has-text("Forms")')
        await page.screenshot(path='doc/screenshots/forms.png')

        # buttons
        await page.goto(context.make_url('/_picocss/components/buttons'))
        await page.wait_for_selector('#lona h1:has-text("Buttons")')
        await page.screenshot(path='doc/screenshots/buttons.png')

        # progress
        await page.goto(context.make_url('/_picocss/components/progress'))
        await page.wait_for_selector('#lona h1:has-text("Progress")')
        await page.screenshot(path='doc/screenshots/progress.png')

        # tabs
        await page.goto(context.make_url('/_picocss/components/tabs'))
        await page.wait_for_selector('#lona h1:has-text("Tabs")')
        await page.screenshot(path='doc/screenshots/tabs.png')

        # modal
        await page.goto(context.make_url('/_picocss/components/modal'))
        await page.wait_for_selector('#lona h1:has-text("Modal")')

        await page.click('a:has-text("Open Modal")')
        await page.wait_for_selector('html.modal-is-visible')

        await page.screenshot(path='doc/screenshots/modal.png')

        # scroller
        await page.goto(context.make_url('/_picocss/components/scroller'))
        await page.wait_for_selector('#lona h1:has-text("Scroller")')
        await page.screenshot(path='doc/screenshots/scroller.png')

        # themes ##############################################################
        for name in ['light', 'dark']:
            await page.goto(context.make_url('/_picocss/settings'))
            await page.wait_for_selector(settings_loaded_selector)

            await page.select_option('select#setting_theme', name)
            await page.wait_for_load_state('load')
            await page.wait_for_selector(settings_loaded_selector)

            await page.screenshot(path=f'doc/screenshots/theme-{name}.png')

        # color schemes #######################################################
        for name in settings.COLOR_SCHEMES.keys():
            await page.goto(context.make_url('/_picocss/settings'))
            await page.wait_for_selector(settings_loaded_selector)

            await page.select_option('select#setting_color-scheme', name)
            await page.wait_for_load_state('load')
            await page.wait_for_selector(settings_loaded_selector)

            await page.screenshot(
                path=f'doc/screenshots/color-scheme-{name}.png',
            )
