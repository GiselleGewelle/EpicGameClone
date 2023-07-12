from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from rest_framework.decorators import action

from .models import Post
from . import serializers
from .permissions import IsAuthor, IsAuthorOrAdmin, IsSeller, IsBuyer


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
<<<<<<< HEAD
        return [permissions.IsAuthenticatedOrReadOnly(), ]

=======
        elif self.action == 'create':
            return [IsSeller(), ]
        return [IsBuyer(), ]
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
