from rest_framework import serializers
from decimal import Decimal
from product.models import Product, Category, Review


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'product_count'
        ]

    product_count = serializers.IntegerField(read_only=True)






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
    

    # field lvl validation while posting
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError('Price cannot be negative')
        return price
    



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            'id',
            'name',
            'description'
        ]

    def create(self, validated_data):
        product_id = self.context['product_id']
        review = Review.objects.create(product_id=product_id, **validated_data)
        return review