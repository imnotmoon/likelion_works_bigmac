from django import forms
from .models import Articles

class ArticleUpdate(forms.ModelForm) :
    class Meta:
        model = Articles
        fields = ['title', 'body']
        print("got values")

