# Buttons

![Buttons](../../doc/screenshots/buttons.png)

```python
from lona_picocss.html import HTML, InlineButton, Button, H1
from lona_picocss import install_picocss
from lona import View, App

app = App(__file__)

install_picocss(app, debug=True)


@app.route('/')
class ButtonsView(View):
    def handle_request(self, request):
        return HTML(
            H1('Buttons'),

            Button('Button'),
            InlineButton('Inline Button', outline=True),
        )


app.run()
```

## Arguments

| Name | Type | Description |
| - | - | - |
| secondary | bool | Secondary styling |
| outline | bool | Outline styling |


## Properties

| Name | Type | Description |
| - | - | - |
| secondary | bool | Secondary styling |
| outline | bool | Outline styling |
