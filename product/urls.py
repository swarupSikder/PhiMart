from django.urls import path
from product import views

urlpatterns = [
    path('products/', views.ViewProducts.as_view(), name='product-list'),
    path('product/<int:pk>/', views.ViewSingleProduct.as_view(), name='view-product'),
    path('categories/', views.ViewCategories.as_view(), name='category-list'),
    path('category/<int:pk>/', views.ViewSingleCategory.as_view(), name='view-category'),
]
