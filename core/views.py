from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForms
def index(request):
  return render(request, 'index.html')

def contact(request):
  
  if request.method == 'POST':
    form = ContactForms(request.POST)
  else:
    form = ContactForms()
  context = {
    'form': form
  }
  return render(request, 'contact.html', context)
