
from django import forms



class ContactForms(forms.Form):
    nome = forms.CharField(label='nome', )
    email = forms.EmailField(label='nome', )
    message = forms.CharField(label='message', widget=forms.Textarea)