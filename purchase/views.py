from rest_framework import generics, permissions
from . import serializers
from .models import Post, Purchase
from .serializers import OrderUserSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class PurchaseCreateView(generics.ListCreateAPIView):
    serializer_class = OrderUserSerializer
    queryset = Purchase.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = serializers.OrderUserSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



