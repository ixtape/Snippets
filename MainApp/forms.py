from django.forms import ModelForm, TextInput, Textarea
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet

        fields = ["name", "lang", "code", "public"]
        labels = {"name": "", "lang": "", "code": "", "public": ""}
        widgets = {
            "name": TextInput(attrs={"placeholder": "Название сниппета"}),
            "code": Textarea(attrs={"placeholder": "Код сниппета"}),
        }

        # С помощью exclude можно указать поля которые нужно исключить
        # Вместе fields и  exclude  использовать нельзя
        # exclude = ['lang']
