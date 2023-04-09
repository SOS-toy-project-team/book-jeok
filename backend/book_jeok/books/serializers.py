from rest_framework import serializers
from .models import Book


class BookSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
