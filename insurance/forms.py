from django import forms


class SearchForm(forms.Form):
    searchTxt = forms.CharField(widget=forms.TextInput(
        attrs={'rows':1,
        'placeholder': 'What is on your mind?'}
    ), max_length=100,label='Search Anything')

 