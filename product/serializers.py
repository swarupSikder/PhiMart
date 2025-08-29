from rest_framework import serializers
from decimal import Decimal
from product.views import Category



class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    # price = serializers.DecimalField(
    #     max_digits=10,
    #     decimal_places=2,
    # )

    # if i wish to show unit_price instead price
    unit_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='price',
    )
    price_with_tax = serializers.SerializerMethodField(
        method_name='calc_tax'
    )
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset = Category.objects.all()
    # )

    # to show the category name directly
    # category = serializers.StringRelatedField()



    def calc_tax(self, product):
        return round(product.price * Decimal(1.1), 2)