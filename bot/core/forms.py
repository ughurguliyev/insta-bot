from django import forms


class UserLogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class SearchForm(forms.Form):
    username = forms.CharField()
    search_title = forms.CharField()
    note = forms.CharField()