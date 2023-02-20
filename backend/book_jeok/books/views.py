from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Book
from .models import Attachment
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.http import Http404

from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .serializers import AttatchmentSerializer

from django.core.paginator import Paginator


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AttachmentViewSet(ModelViewSet):
    serializer_class = AttatchmentSerializer
    queryset = Attachment.objects.all()

