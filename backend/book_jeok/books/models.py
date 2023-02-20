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


class Attachment(models.Model):
    """책 첨부파일 모델"""
    file_no = models.BigAutoField(primary_key=True)  # pk로 설정
    path = models.CharField(max_length=255)
    book_id = models.ForeignKey('books.Book')
    """FileField라는 파일관련 모델 필드가 있어서 혹시 몰라 주석 처리 해서 넣어놨습니다."""
    # path = models.FileField()
