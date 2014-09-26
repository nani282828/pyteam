from django import forms

class PostStatusForm(forms.Form):
    user_post = forms.CharField()
