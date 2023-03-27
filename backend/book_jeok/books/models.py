from django.db import models

# Create your models here.


class Book(models.Model):
    """책 모델"""
    book_id = models.BigAutoField(primary_key=True)  # pk로 설정
    title = models.CharField(max_length=255) # API 책이름
    publisher = models.CharField(max_length=255) # API 출판사
    # genre = models.CharField(max_length=255) # API로 못가져옴
    author = models.CharField(max_length=255) # API 작가이름
    description = models.CharField(max_length=255) # API 간단 설명
    pubdate = models.DateTimeField() # API 출간일
    path = models.CharField(max_length=255)