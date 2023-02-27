from django.db import models


class Review(models.Model):
    """리뷰 모델"""
    review_id = models.BigAutoField(primary_key=True)  # pk로 설정
    book_id = models.ForeignKey('books.Book', on_delete=models.CASCADE)
    user_id = models.ForeignKey('signin.book_user', on_delete=models.CASCADE)
    # user_id = models.ForeignKey('User', on_delete=models.CASCADE) # 임시 USER 연결
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()
    star_point = models.IntegerField()

# class User(models.Model):
#     """임시 User 모델"""
#     user_id = models.BigAutoField(primary_key=True)  # pk로 설정
#     user_name = models.CharField(max_length=10)
#     user_nickname = models.CharField(max_length=10)
#     user_login_id = models.CharField(max_length=10)
#     user_pw = models.CharField(max_length=10)

class Comment(models.Model):
    """리뷰에 달릴 댓글 모델"""
    comment_id = models.BigAutoField(primary_key=True)  # pk로 설정
    review_id = models.ForeignKey('Review', on_delete=models.CASCADE)
    user_id = models.ForeignKey('signin.book_user', on_delete=models.CASCADE)
    # user_id = models.ForeignKey('User', on_delete=models.CASCADE) # 임시 USER 연결
    created_time = models.DateField(auto_now_add=True)
    content = models.TextField()

