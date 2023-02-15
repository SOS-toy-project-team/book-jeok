from django.db import models

# Create your models here.

class book_user(models.Model): #유저 정보
    user_id=models.CharField(max_length=10,unique=True) #아이디
    user_pw=models.CharField(max_length=10) #비밀번호
    