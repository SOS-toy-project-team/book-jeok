from rest_framework import serializers

from books.serializers import BookSerializer
from .models import Review,Comment,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    book_id = BookSerializer()
    user_id = UserSerializer()

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializerSave(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()

    class Meta:
        model = Comment
        fields = "__all__"

class CommentSerializerSave(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"