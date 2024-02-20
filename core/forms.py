
from django import forms
from django.core.mail import send_mail
from django.conf import settings

class ContactForms(forms.Form):
    nome = forms.CharField(label='nome', )
    email = forms.EmailField(label='email', )
    message = forms.CharField(label='message', widget=forms.Textarea)
    
    
    # def __ini__(self, *args, **kwargs):
    #     super(ContactForms, self).__init__(*args, **kwargs)
    #     self.fields['nome'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'
    
    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        
        # i need to configure this
        # send_mail(subject=nome, message=message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.DEFAULT_FROM_EMAIL])