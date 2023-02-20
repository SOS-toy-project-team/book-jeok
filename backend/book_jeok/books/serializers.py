from rest_framework import serializers
from .models import Book
from .models import Attachment


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class AttatchmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attachment
        fields = "__all__"