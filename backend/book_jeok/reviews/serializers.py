from rest_framework import serializers

from books.serializers import BookSerializer
from .models import Review, Comment
from signin.models import book_user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = book_user
        fields = ["user_id", "user_nickname"]


class ReviewSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True, source='book_id')
    user = UserSerializer(read_only=True, source='user_id')

    class Meta:
        model = Review
        exclude = ["book_id", "user_id"]


class ReviewSerializerSave(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_id')

    class Meta:
        model = Comment
        fields = ["comment_id", "user", "content", "created_time"]


class CommentSerializerSave(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"