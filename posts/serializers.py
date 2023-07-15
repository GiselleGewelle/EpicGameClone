from random import randint

from rest_framework import serializers
from category.models import Category
from comment.serializers import CommentSerializer
from posts.models import Post, PostImages


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Post
        fields = (
            'id', 'owner', 'owner_email', 'title_of_game', 'price', 'date_of_issue', 'images', 'link_on_game',
            'video')


class PostSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    owner = serializers.ReadOnlyField(source='owner.id')
    images = PostImageSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        images = request.FILES.getlist('images')
        post = Post.objects.create(**validated_data)
        for image in images:
            PostImages.objects.create(image=image, post=post)
        return post

    #
    # class PostImageSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = PostImages
    #         fields = '__all__'
    #
    #
    # class PostCreateSerializer(serializers.ModelSerializer):
    #     category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())
    #     owner = serializers.ReadOnlyField(source='owner.id')
    #     images = PostImageSerializer(many=True, required=False)
    #
    #     class Meta:
    #         model = Post
    #         fields = '__all__'
    #
    #     def create(self, validated_data):
    #         request = self.context.get('request')
    #         images = request.FILES.getlist('images')
    #         post = Post.objects.create(**validated_data)
    #         for image in images:
    #             PostImages.objects.create(image=image, post=post)
    #         return post

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['comments_count'] = instance.comments.count()
        repr['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        repr['likes_count'] = instance.likes.count()
        user = self.context['request'].user
        if user.is_authenticated:
            repr['is_liked'] = user.likes.filter(post=instance).exists()
            repr['is_favorite'] = user.favorites.filter(post=instance).exists()
        return repr


class FavoriteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr["author"] = instance.author.email
        repr["category"] = instance.category.title
        return repr
