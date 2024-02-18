from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, TemplateView

from .forms import ContactForms
# def index(request):
#   return render(request, 'index.html')


class IndexView(TemplateView): 
  template_name = 'index.html'

index = IndexView.as_view()


class ContactView(View):
  
  def __init__(self):
    self.context = {'success': False, 'form': ContactForms()}
  
  def get(self, request):
    return render(request, 'contact.html', context=self.context)
  
  def post(self, request):
    self.context['form'] = ContactForms(request.POST)
    if self.context['form'].is_valid():
      self.context['success'] = True
    return render(request, 'contact.html', context=self.context)

contact = ContactView.as_view()
