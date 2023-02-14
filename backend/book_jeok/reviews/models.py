from django.db import models


class Review(models.Model):
    """리뷰 모델"""
    review_id = models.BigAutoField(primary_key=True)  # pk로 설정
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    liked = models.PositiveIntegerField()


class Comments(models.Model):
    """리뷰에 달릴 댓글 모델"""
    comments_id = models.BigAutoField(primary_key=True)  # pk로 설정
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()


# class Books(models.Model):
#     """책 모델"""
#     book_id = models.BigAutoField(primary_key=True)  # pk로 설정
#     title = models.CharField(max_length=255)
#     publisher = models.CharField(max_length=255)
#     genre = models.CharField(max_length=255)
#
#
# class Attachments(models.Model):
#     """책 첨부파일 모델"""
#     file_no = models.BigAutoField(primary_key=True)  # pk로 설정
#     path = models.CharField(max_length=255)
#     """FileField라는 파일관련 모델 필드가 있어서 혹시 몰라 주석 처리 해서 넣어놨습니다."""
#     # path = models.FileField()