from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

product_list = ProductListView.as_view()

class CategoryListView(ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context
    

category = CategoryListView.as_view()

# def category(request, slug):
#     cat = Category.objects.get(slug=slug)
#     context = {
#         'products': Product.objects.filter(category=cat),
#         'current_category': cat
#     }
#     return render(request, 'catalog/category.html', context)

def product(request, slug_product):
    context = {
        'product': Product.objects.get(slug=slug_product),
    }
    return render(request, 'catalog/product.html', context)