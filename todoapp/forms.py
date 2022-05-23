from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

