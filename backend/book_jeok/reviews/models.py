from django.db import models


class Review(models.Model):
    """리뷰 모델"""
    review_id = models.BigAutoField(primary_key=True)  # pk로 설정
    title = models.CharField(max_length=255)
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    liked = models.PositiveIntegerField()


class Comments(models.Model):
    """리뷰에 달릴 댓글 모델"""
    comments_id = models.BigAutoField(primary_key=True)  # pk로 설정
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
