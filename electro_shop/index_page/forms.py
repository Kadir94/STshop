from django import forms

from .models import SearchModel


class SearchForm(forms.ModelForm):
    class Meta:
        model = SearchModel
        fields = '__all__'
        widgets = {
            'search': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search'})
        }
        labels = {
            'search': ''
        }
