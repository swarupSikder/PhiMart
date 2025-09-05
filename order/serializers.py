from rest_framework import serializers
from order.models import Cart, CartItem
from product.models import Product
from product.serializers import ProductSerializer



class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price'
        ]

class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField('get_total_price')
    
    class Meta:
        model = CartItem
        fields = [
            'id',
            'product',
            'quantity',
            'product',
            'total_price'
        ]

    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity*cart_item.product.price


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_cart_price = serializers.SerializerMethodField(
        method_name='get_total_cart_price'
    )

    class Meta:
        model = Cart 
        fields = [
            'id',
            'user',
            'items',
            'total_cart_price'
        ]

    def get_total_cart_price(self, cart: Cart):
        list = sum([item.product.price*item.quantity for item in cart.items.all()])
        # print("list", list)
        return list