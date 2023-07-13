from rest_framework import serializers
from category.models import Category
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Post
        fields = (
            'id', 'owner', 'owner_email', 'title_of_game', 'price', 'date_of_issue', 'image_for_full', 'link_on_game',
            'slug', 'video')


class PostSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Post
        fields = '__all__'
