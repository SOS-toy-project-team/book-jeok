from rest_framework import serializers

from books.serializers import BookSerializer
from .models import Review,Comment,User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    book_id = BookSerializer(read_only=True)
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    user_id = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"