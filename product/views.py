from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Count
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter



# - - - - - - - - - - - #
#      All Products     #
# - - - - - - - - - - - #
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # filterset_fields = ['category_id', 'price']
    filterset_class = ProductFilter
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['price']

    # def get_queryset(self):
    #     queryset = Product.objects.all()
    #     category_id = self.request.query_params.get('category_id')

    #     if category_id is not None:
    #         queryset = Product.objects.filter(category_id=category_id)

    #     return queryset
        

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







class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])
    

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}