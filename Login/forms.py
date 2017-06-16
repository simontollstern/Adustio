from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=150)
    text = forms.CharField(label='Text', max_length=15000)
    date = forms.DateField(label='Date')
