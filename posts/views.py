from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from rest_framework.decorators import action

from .models import Post
from . import serializers
from .permissions import IsAuthor, IsAuthorOrAdmin, IsSeller, IsBuyer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


# class PostDeleteView(APIView):
#     def delete(self, request, slug):
#         my_model = get_object_or_404(Post, slug=slug)
#         my_model.delete()
#         return Response("Object deleted successfully.")


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer
        return serializers.PostSerializer

    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAuthorOrAdmin(), ]
        elif self.action in ('update', 'partial_update'):
            return [IsAuthor(), ]
        elif self.action == 'create':
            return [IsSeller(), ]
        elif self.action == 'list':
            return [permissions.AllowAny(), ]
        return [IsBuyer(), ]
