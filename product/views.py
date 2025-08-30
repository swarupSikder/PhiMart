from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView





# - - - - - - - - - - - #
#      All Products     #
# - - - - - - - - - - - #
class ProductList(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer

    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializer

    # def get_serializer_context(self):
    #     return {'request': self.request}




# - - - - - - - - - - - - - #
#    Single Product View    #
# - - - - - - - - - - - - - #
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if product.stock >= 10:
            return Response({'message': 'Product with stock of more than 10 cannot be deleted!!!'})
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)








# - - - - - - - - - - - - - #
#     View All Categories   #
# - - - - - - - - - - - - - #
class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer




# - - - - - - - - - - - - - #
#     View Single Category  #
# - - - - - - - - - - - - - #
class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer