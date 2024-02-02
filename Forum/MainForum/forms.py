from django import forms
from .models import Ghost


class AddGhostSearchForm(forms.Form):
    name = forms.ModelChoiceField(
        queryset=Ghost.objects.all(),
        label='Имя призрака',
        empty_label='Выбери призрака!')