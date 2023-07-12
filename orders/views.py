from rest_framework import generics, permissions
from . import serializers
from .models import Post, Order
from .serializers import OrderUserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class OrderCreateView(generics.ListCreateAPIView):
    serializer_class = OrderUserSerializer
    queryset = Order.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.OrderUserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



