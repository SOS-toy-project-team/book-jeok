from django.db import models

# Create your models here.

class book_user(models.Model): #유저 정보
    user_name=models.CharField(max_length=10,unique=True,default="") #닉네임
    user_id=models.CharField(max_length=10,unique=True,default="") #아이디
    user_pw=models.CharField(max_length=10,default="") #비밀번호
    