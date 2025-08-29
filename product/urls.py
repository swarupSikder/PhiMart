from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.view_products, name='product-list'),
    path('product/<int:pk>/', views.view_single_product, name='view-product'),
    path('categories/', views.view_categories, name='category-list'),
    path('category/<int:pk>/', views.view_single_category, name='view-category'),
]
