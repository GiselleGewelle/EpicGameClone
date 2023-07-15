<<<<<<< HEAD
from django.views.decorators.cache import cache_page
from rest_framework import generics, permissions
from posts.permissions import IsAuthorOrAdminOrPostOwner
=======
from rest_framework import generics, permissions
from posts.permissions import IsAuthorOrAdmin
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
from .models import Comment
from . import serializers


class CommentCreateView(generics.CreateAPIView):
<<<<<<< HEAD
    serializer_class = serializers.CommentSerializers
=======
    serializer_class = serializers.CommentSerializer
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
<<<<<<< HEAD
    serializer_class = serializers.CommentSerializers

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthorOrAdminOrPostOwner(), ]
=======
    serializer_class = serializers.CommentSerializer

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsAuthorOrAdmin(), ]
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
        return [permissions.AllowAny(), ]
