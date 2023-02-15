from django.shortcuts import render
from rest_framework import status

from .models import Review
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewSerializer


class ReviewSimple(APIView):

    """모든 리뷰들을 보내줌"""
    def get(self, request):
        all_review = Review.objects.all()
        serializer = ReviewSerializer(all_review, many=True)
        return Response(serializer.data)

    """ request data에 user_id, book_id가 담겨와야함 """
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewUser(APIView):

    """ user_id에 해당하는 게시글들을 보내줌 """
    def get(self, request, user_id):
        # reviews = Review.objects.filter(user_id=user_id)
        reviews = Review.objects.filter(review_id=user_id) # 임시 작동 확인용
        serializer = ReviewSerializer(reviews, many = True)
        return Response(serializer.data)


class ReviewDetail(APIView):
    """review_id에 해다하는 게시글 수정(user_id가 동일한지 검증 필요)"""
    def put(self, request, review_id):
        # review = Review.objects.get(review_id=review_id)
        reviews = Review.objects.filter(review_id=user_id) # 임시 작동 확인용
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







