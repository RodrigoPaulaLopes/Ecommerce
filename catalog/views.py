from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from .models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 3

product_list = ProductListView.as_view()

class CategoryListView(ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'products'
    paginate_by = 3
    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
    
    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context
    

category = CategoryListView.as_view()


class ProductView(ListView):

    template_name = 'catalog/product.html'
    context_object_name = 'product'
    def get_queryset(self):
        return Product.objects.get(slug=self.kwargs['slug_product'])
    
product = ProductView.as_view()
