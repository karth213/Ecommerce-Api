from rest_framework import serializers
from .models import User, Order, OrderItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        extra_kwargs = {'password': {'write_only': True}}
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            return user 
        
        def update(self, instance, validated_data):
            instance.first_name = validated_data.get('first_name', instance.first_name)
            instance.last_name = validated_data.get('last_name', instance.last_name)
            instance.email = validated_data.get('email', instance.email)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.place = validated_data.get('place', instance.place)
            instance.save()
            return instance
        

class OrderItemSerialzer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem  
        fields = (
            '__all__'
        )     


class OrderSerilazer(serializers.ModelSerializer):
    items = OrderItemSerialzer(many= True)
    class Meta:
        model = Order
        fields = (
            'id', 
            'first_name',
            'last_name',
            'email', 
            'phone',
            'created_at',
            'paid_amount',
            'stripe_token',
            'items',
        )

        def create(self, validated_data):
            items_data = validated_data.pop('items',)
            order = Order.objects.create(**validated_data)

            for item_data in items_data:
                OrderItem.objects.create(order=order, **item_data)
            return order



