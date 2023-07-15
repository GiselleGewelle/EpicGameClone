from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, response, status
from rest_framework.decorators import action

from .models import Post, Likes, Favorite
from . import serializers
from .permissions import IsAuthor, IsAuthorOrAdmin, IsSeller, IsBuyer

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import PostSerializer


# class PostDeleteView(APIView):
#     def delete(self, request, slug):
#         my_model = get_object_or_404(Post, slug=slug)
#         my_model.delete()
#         return Response("Object deleted successfully.")

class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    pagination_class = StandartResultPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('title_of_game', 'title_of_publisher')
    filterset_fields = ('owner', 'category')

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

    @action(detail=True, methods=['GET'])
    def toggle_like(self, request, pk):
        post = self.get_object()
        user = request.user
        like_obj, created = Likes.objects.get_or_create(post=post, user=user)

        like_obj.is_liked = not like_obj.is_liked
        like_obj.save()
        return Response('like toggled')

    @action(detail=False, methods=["GET"])
    def likes(self, request, pk=None):
        from django.db.models import Count
        q = request.query_params.get("likes_from")  # request.query_params = request.GET
        queryset = self.get_queryset()
        queryset = queryset.annotate(Count('likes')).filter(likes__count__gte=q)

        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_context(self):
        return {'request': self.request}

    @action(detail=True, methods=['GET'])
    def toggle_favorites(self, request, pk):
        post = self.get_object()
        user = request.user
        fav, created = Favorite.objects.get_or_create(post=post, user=user)

        fav.favorite = not fav.favorite
        fav.save()
        return Response('favourite toggled')