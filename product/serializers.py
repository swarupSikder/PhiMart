from rest_framework import serializers
from decimal import Decimal
from product.views import Category, Product


# class CategorySerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     description = serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'product_count'
        ]
    
    # product_count = serializers.SerializerMethodField(
    #     method_name='get_product_count'
    # )

    # def get_product_count(self, category):
    #     count = Product.objects.filter(category=category).count()
    #     return count

    product_count = serializers.IntegerField()




# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField()
#     # price = serializers.DecimalField(
#     #     max_digits=10,
#     #     decimal_places=2,
#     # )

#     # if i wish to show unit_price instead price
#     unit_price = serializers.DecimalField(
#         max_digits=10,
#         decimal_places=2,
#         source='price',
#     )
#     price_with_tax = serializers.SerializerMethodField(
#         method_name='calc_tax'
#     )
#     # category = serializers.PrimaryKeyRelatedField(
#     #     queryset = Category.objects.all()
#     # )

#     # to show the category name directly
#     # category = serializers.StringRelatedField()

#     # to show Categories/Category
#     # category = CategorySerializer()

#     # to show categories/category hyperlink
#     category = serializers.HyperlinkedRelatedField(
#         queryset = Category.objects.all(),
#         view_name = 'view-category'
#     )


#     def calc_tax(self, product):
#         return round(product.price * Decimal(1.1), 2)



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = [
            'id', 
            'name', 
            'description', 
            'price', 
            'stock', 
            'category', 
            'price_with_tax'
        ]

    price_with_tax = serializers.SerializerMethodField(
        method_name='calc_tax'
    )

    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name = 'view-category'
    # )

    def calc_tax(self, product):
        return round(product.price * Decimal(1.1), 2)