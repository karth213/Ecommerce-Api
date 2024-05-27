from rest_framework import serializers

from . models import Product, Category
from Orderapp.models import OrderItem, Order


class ProdocutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 
            'name',
            'get_absolute_url',
            'description',
            'price',
            'get_image',
            'get_thumnail'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 
            'Name',
            'get_absolute_url',
        )

# class OrderItemSerilazer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = (
#             'order',
#             'product',
#             'price',
#             'quntity'
            
#         )

# class OrderSerilazer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ['__all__']