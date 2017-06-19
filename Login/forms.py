from django import forms

class AddPostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=150)
    text = forms.CharField(label='Text', max_length=15000)
    youtube = forms.CharField(label='Youtube-video (optional)', required=False)
    soundcloud = forms.CharField(label='Soundcloud track (optional)', required=False)
    #date = forms.DateTimeField(label='Date')

class EditPostForm(forms.Form):
    title = forms.CharField(label='Title', max_length=150)
    text = forms.CharField(label='Text', max_length=15000)
    youtube = forms.CharField(label='Youtube-video (optional)', required=False)
    soundcloud = forms.CharField(label='Soundcloud track (optional)', required=False)
    #date = forms.DateTimeField(label='Date')
