from django import forms

from .models import SearchModel,JsonModel


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = '__all__'
        widgets = {
            'search': forms.TextInput(attrs={'id': 'searchinput', 'placeholder': 'Search'})
        }
        labels = {
            'search': ''
        }


class JsonForm(forms.ModelForm):
    class Meta:
        model = JsonModel
        fields = '__all__'
