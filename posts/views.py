from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response
from rest_framework.decorators import action
from .models import Post
from . import serializers
from .permissions import IsAuthor, IsAuthorOrAdmin, IsSeller, IsBuyer
from rest_framework.response import Response
from rating.serializers import MarkSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.PostListSerializer
        return serializers.PostSerializer

    @action(methods=['POST', 'GET'], detail=True)
    def rating(self, request, pk):
        post = self.get_object()
        if request.method == 'GET':
            marks = post.marks.all()
            serializer = MarkSerializer(marks, many=True).data
            return response.Response(serializer, status=200)
        elif post.marks.filter(owner=request.user).exists():
                return response.Response('You already marked this post!',
                                         status=400)
        elif request.method == 'POST':
            Mark.objects.create(owner=request.user, mark=request.data['mark'], post=post)
            return response.Response({'msg': 'Thank you for your mark'}, status=201)
    @action(['DELETE'], detail=True)
    def rating_delete(self, request, pk):
        post = self.get_object()  # Product.objects.get(id=pk)
        user = request.user
        if not post.marks.filter(owner=user).exists():
            return response.Response('You didn\'t marked this post!',
                                     status=400)
        mark = post.marks.get(owner=user)
        mark.delete()
        return response.Response('Successfully deleted', status=204)


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

