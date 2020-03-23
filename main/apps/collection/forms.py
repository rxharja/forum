from django import forms

class SearchForm(forms.Form):
    your_search = forms.CharField(label='Your Search', max_length=100)
