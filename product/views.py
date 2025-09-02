from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet





# - - - - - - - - - - - #
#      All Products     #
# - - - - - - - - - - - #
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, *args, **kwargs):
        product = self.get_object()   #instance
        if product.stock >= 10:
            return Response({'message': 'Product with stock of more than 10 cannot be deleted!!!'})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)




# - - - - - - - - - - - - - #
#     View All Categories   #
# - - - - - - - - - - - - - #
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer