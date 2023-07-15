from rest_framework import serializers
from .models import Comment


<<<<<<< HEAD
class CommentSerializers(serializers.ModelSerializer):
=======
class CommentSerializer(serializers.ModelSerializer):
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = '__all__'
<<<<<<< HEAD

=======
>>>>>>> cfe1ff339981fd4d4db7fd79f3641866c653f889
