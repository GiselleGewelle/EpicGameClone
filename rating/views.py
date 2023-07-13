from rest_framework import generics, permissions
from . import serializers
from .models import Mark
from posts.permissions import IsAuthor


class MarkCreateView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.MarkSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MarkDeleteView(generics.DestroyAPIView):
    queryset = Mark.objects.all()
    permission_classes = (IsAuthor, )
