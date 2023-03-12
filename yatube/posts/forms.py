from django import forms

class PostForm(forms.Form):
    text = forms.CharField(label='text', max_length=1000, required=True)
    group = forms.CharField(label='group', max_length=100)