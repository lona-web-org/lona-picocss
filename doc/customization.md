# Customization

lona-picocss comes with a visual theme configuratior built-in.
Make sure you [installed](./getting-started.md#getting-started) lona-picocss with `debug` set to `True`, and go to `/_picocss/settings`.
The configurator applies all changes live. After you are done, copy all settings from `Compiled Settings` into your script, to make your changes permanent.

![](../doc/screenshots/settings.png)


## Menu

The default template of lona-picocss has support for a menu at the top. To configurate its contents set `settings.PICOCSS_MENU`, like in this example.
When `app.settings.PICOCSS_MENU` is set to an empty list, the menu does not get rendered.

```python
app.settings.PICOCSS_MENU = [
    ['Simple Link', '/home'],
    ['Dropdown', [
        ['Dropdown Link 1', '/dropdown/link-1/'],
        ['Dropdown Link 1', '/dropdown/link-1/'],
    ]],
    ['Reverse URL', '!picocss__settings'],
]
```


## Themes

lona-picocss has support for light and dark themes

### Light
![](../doc/screenshots/theme-light.png)

### Dark
![](../doc/screenshots/theme-dark.png)


## Color Schemes

lona-picocss has support for a list of different color schemes. All of them can be used with light- and dark theme.

### Amber
![](../doc/screenshots/color-scheme-amber.png)

### Blue
![](../doc/screenshots/color-scheme-blue.png)

### Blue Grey
![](../doc/screenshots/color-scheme-blue-grey.png)

### Cyan
![](../doc/screenshots/color-scheme-cyan.png)

### Deep Orange
![](../doc/screenshots/color-scheme-deep-orange.png)

### Deep Purple
![](../doc/screenshots/color-scheme-deep-purple.png)

### Green
![](../doc/screenshots/color-scheme-green.png)

### Gray
![](../doc/screenshots/color-scheme-gray.png)

### Indigo
![](../doc/screenshots/color-scheme-indigo.png)

### Light Blue
![](../doc/screenshots/color-scheme-light-blue.png)

### Light Green
![](../doc/screenshots/color-scheme-light-green.png)

### Lime
![](../doc/screenshots/color-scheme-lime.png)

### Orange
![](../doc/screenshots/color-scheme-orange.png)

### Pink
![](../doc/screenshots/color-scheme-pink.png)

### Purple
![](../doc/screenshots/color-scheme-purple.png)

### Red
![](../doc/screenshots/color-scheme-red.png)

### Teal
![](../doc/screenshots/color-scheme-teal.png)

### Yellow
![](../doc/screenshots/color-scheme-yellow.png)
