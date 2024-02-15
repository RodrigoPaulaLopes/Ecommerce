from django.shortcuts import render

# Create your views here.

from .models import Product, Category
def product_list(request):
    
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'catalog/product_list.html', context)

def category(request, slug):
    cat = Category.objects.get(slug=slug)
    context = {
        'products': Product.objects.filter(category=cat),
        'current_category': cat
    }
    return render(request, 'catalog/category.html', context)