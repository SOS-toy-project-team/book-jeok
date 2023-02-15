from django.db import models


class Review(models.Model):
    """리뷰 모델"""
    review_id = models.BigAutoField(primary_key=True)  # pk로 설정
    book_id = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    # user_id = models.ForeignKey('users.User') # User 테이블이 만들어지면 추가 예정
    title = models.CharField(max_length=255)
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    liked = models.PositiveIntegerField()


class Comment(models.Model):
    """리뷰에 달릴 댓글 모델"""
    comments_id = models.BigAutoField(primary_key=True)  # pk로 설정
    review_id = models.ForeignKey('Review', on_delete=models.CASCADE)
    # user_id = models.ForeignKey('users.User') # User 테이블이 만들어지면 추가 예정
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
