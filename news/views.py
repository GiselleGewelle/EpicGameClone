from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from . import serializers
from .models import News
from .tasks import parsing


# Ваш ViewSet для модели News
class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = serializers.NewsSerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [permissions.AllowAny(), ]
        return [permissions.IsAdminUser(), ]

    @action(detail=False, methods=['GET'])
    def parse_news(self, request, *args, **kwargs):
        parsing.delay()
        return Response('Parse done')
