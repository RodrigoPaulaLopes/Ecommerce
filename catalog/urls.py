from django.urls import path

from .views import product_list, category, product


urlpatterns = [
    path("", product_list, name='catalogo'),
    path("<str:slug>", category, name='catalogo'),
    path("produtos/<str:slug_product>", product, name='catalogo')
]
