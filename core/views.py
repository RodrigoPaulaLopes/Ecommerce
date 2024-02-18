from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForms
def index(request):
  return render(request, 'index.html')

def contact(request):
  form = ContactForms(request.POST or None)
  success = False
  if form.is_valid():
    success = True
  form = ContactForms()
  context = {
    'form': form,
    'success': success
  }
  return render(request, 'contact.html', context)
