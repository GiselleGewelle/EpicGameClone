from rest_framework import generics, permissions
from . import serializers
from .models import Mark
from rest_framework import serializers

from rating.models import Mark


class MarkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user.email')
    post = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Mark
        fields = '__all__'

    def validate(self, attrs):
        user = self.context['request'].user
        post = attrs['post']

        if user.marks.filter(post=post).exists():
            raise serializers.ValidationError('You already marked this post')
        return attrs