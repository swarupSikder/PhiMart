from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name='view-product'),
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetails.as_view(), name='view-category'),
]
