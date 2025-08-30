from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.generics import ListCreateAPIView








# - - - - - - - - - - - #
#      All Products     #
# - - - - - - - - - - - #
class ViewProducts(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # Deserializer
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


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
class ViewSingleProduct(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def put(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# - - - - - - - - - - - - - #
#     View All Categories   #
# - - - - - - - - - - - - - #
class ViewCategories(APIView):
    def get(self, request):
        categories = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializer




# - - - - - - - - - - - - - #
#     View Single Category  #
# - - - - - - - - - - - - - #
class ViewSingleCategory(APIView):
    def get(self, request, pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')),
            pk=pk
        )
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')),
            pk=pk
        )
        serializer = CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')),
            pk=pk
        )
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)