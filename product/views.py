from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializer

# - - - - - - - - - - - #
#      All Products     #
# - - - - - - - - - - - #
@api_view()
def view_products(request):
    products = Product.objects.select_related('category').all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)





# - - - - - - - - - - - - - #
#    Single Product View    #
# - - - - - - - - - - - - - #
@api_view()
def view_single_product(request, id):
    product = get_object_or_404(Product, pk=id)
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
    return Response({'message': "categories"})