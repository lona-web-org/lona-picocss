from lona import View


class ItWorksView(View):
    def handle_request(self, request):
        return """
            <h1>It works!</h1>
            <p><strong>Next Steps:</strong></p>
            <ul>
                <li><a href="https://lona-web.org/" data-lona-ignore=True>Lona Documentation</a></li>
                <li><a href="https://github.com/lona-web-org/lona-picocss" data-lona-ignore=True>Lona Pico.css Documentation</a></li>
            </ul>
        """
