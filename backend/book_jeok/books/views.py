from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from book_jeok import settings
from .models import Book
from .models import Attachment
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import status
from django.http import Http404
from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer
from .serializers import AttatchmentSerializer
from django.http import JsonResponse

# API
import os
import sys
import urllib.request
import json

class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AttachmentViewSet(ModelViewSet):
    serializer_class = AttatchmentSerializer
    queryset = Attachment.objects.all()


# API book search
# book api
def api_book_search(request):
    if request.method == 'GET':
        config_secret_debug = json.loads(open(settings.SECRET_DEBUG_FILE).read())
        client_id = config_secret_debug['NAVER']['CLIENT_ID']
        client_secret = config_secret_debug['NAVER']['CLIENT_SECRET']

        q = request.GET.get('q')  # q로 검색 키워드를 가져옵니당~
        encText = urllib.parse.quote("{}".format(q))  # 검색된 단어
        url = "https://openapi.naver.com/v1/search/book?query=" + encText  # json 결과
        book_api_request = urllib.request.Request(url)
        book_api_request.add_header("X-Naver-Client-Id", client_id)
        book_api_request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(book_api_request)
        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            result = json.loads(response_body.decode('utf-8'))
            items = result.get('items') # item 당 title, image, author, publisher

            context = {
                'items': items
            }
            return JsonResponse(context)
        else:
            code = {
                'code': rescode
            }
            return JsonResponse(code)
