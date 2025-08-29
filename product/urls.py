from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.view_products, name='product-list'),
    path('product/<int:id>/', views.view_single_product, name='view-product'),
    path('categories/', views.view_categories, name='category-list'),
]
