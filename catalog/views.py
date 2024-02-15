from django.shortcuts import render

# Create your views here.

from .models import Product
def product_list(request):
    
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)