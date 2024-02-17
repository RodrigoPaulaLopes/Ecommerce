
from django import forms



class ContactForms(forms.Form):
    nome = forms.CharField(label='nome', )
    email = forms.EmailField(label='email', )
    message = forms.CharField(label='message', widget=forms.Textarea)
    
    
    # def __ini__(self, *args, **kwargs):
    #     super(ContactForms, self).__init__(*args, **kwargs)
    #     self.fields['nome'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'