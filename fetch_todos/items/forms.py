
from django import forms

class ItemForm(forms.Form):
    item = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for label, field in self.fields.items():
            field.widget.attrs.update({
                "placeholder": "Add a todo...",
                "class": "form_element",
                "id": "input_text",
            })
