from rest_framework import serializers

from orders.models import Order


class OrderUserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Order
        fields = '__all__'
