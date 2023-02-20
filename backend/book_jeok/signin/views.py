from django.shortcuts import render
from django.views import View
import json
from django.db.models import Q
from json.decoder import JSONDecodeError
from django.http import JsonResponse
from .models import book_user
# Create your views here.

class SignUpView(View):
    def post(self,req):
        try:
            data=json.loads(req.body)

            user_name=data.get('user_name',None) #닉네임
            user_id=data.get('user_id',None) #아이디
            user_pw=data.get('user_pw',None) #비밀번호

            book_user.objects.create(
                user_name=user_name,
                user_id=user_id, 
                user_pw=user_pw
            )
            
            return JsonResponse({'message':'SUCCESS'},status=201)
        except JSONDecodeError:
            return JsonResponse({'message':'JSON_DECODE_ERROR'},status=400)
