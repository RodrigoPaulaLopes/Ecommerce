from django.urls import path

from .views import product_list, category

urlpatterns = [
    path("", product_list, name='produtos'),
    path("<str:slug>", category, name='produtos')
]
