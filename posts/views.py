from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from rest_framework.decorators import action

from .models import Post
from . import serializers
from .permissions import IsAuthor, IsAuthorOrAdmin, IsSeller, IsBuyer
from rest_framework.response import Response
from rating.serializers import MarkSerializer
from rating.models import Mark


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer
        return serializers.PostSerializer

    @action(methods=['POST'], detail=True)
    def rating(self, request, pk):
        product = self.get_object()
        if request.method == 'GET':
            marks = product.marks.all()
            serializer = MarkSerializer(marks, many=True).data
            return response.Response(serializer, status=200)
        else:
            if product.marks.filter(user=request.user).exists():
                return response.Response('You already marked this product!',
                                         status=400)
            data = request.data  # rating text
            serializer = MarkSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user, product=product)
            return response.Response(serializer.data, status=201)



    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAuthorOrAdmin(), ]
        elif self.action in ('update', 'partial_update'):
            return [IsAuthor(), ]
        elif self.action == 'create':
            return [IsSeller(), ]
        return [IsBuyer(), ]

