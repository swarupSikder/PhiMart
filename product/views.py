from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer
from django.db.models import Count

# - - - - - - - - - - - #
#      All Products     #
# - - - - - - - - - - - #
@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        # serializer = ProductSerializer(products, many=True, context={'request':request})
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data) # Deserializer
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# - - - - - - - - - - - - - #
#    Single Product View    #
# - - - - - - - - - - - - - #
@api_view()
def view_single_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
    
    # try:
    #     product = Product.objects.get(pk=id)
    #     product_dict = {
    #         'id': product.id,
    #         'name': product.name,
    #         'price': product.price,
    #     }
    #     return Response({'product': product_dict})
    # except Product.DoesNotExist:
    #     return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)





# - - - - - - - - - - - - - #
#     View All Categories   #
# - - - - - - - - - - - - - #
@api_view()
def view_categories(request):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(product_count=Count('products')).all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)





# - - - - - - - - - - - - - #
#     View Single Category  #
# - - - - - - - - - - - - - #
@api_view()
def view_single_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data)