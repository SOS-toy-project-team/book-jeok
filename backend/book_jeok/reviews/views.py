from django.shortcuts import render
from rest_framework import status

from .models import Review, Comment
from books.models import Attachment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewSerializer, CommentSerializer
from books.serializers import AttatchmentSerializer


class ReviewSimple(APIView):

    """모든 리뷰들을 보내줌"""
    def get(self, request):
        all_review = Review.objects.select_related('book_id', 'user_id')
        serializer = ReviewSerializer(all_review, many=True)
        return Response(serializer.data)

    """ request data에 user_id, book_id가 담겨와야함 """
    def post(self, request):
        request.data.get()
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewByUser(APIView):

    """ user_id에 해당하는 게시글들을 보내줌 """
    def get(self, request, user_id):
        reviews = Review.objects.select_related('book_id', 'user_id').filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewById(APIView):
    """review_id에 해당하는 게시글 관련 클래스"""
    def get(self, request, review_id):
        review = Review.objects.select_related('book_id', 'user_id').filter(review_id=review_id)
        comments = Comment.objects.select_related('review_id').filter(review_id=review_id)
        attachment = Attachment.objects.filter(book_id=Review.objects
                                               .filter(review_id=review_id).values('book_id').get()['book_id'])
        review_serializer = ReviewSerializer(review, many=True)
        comments_serializer = CommentSerializer(comments, many=True)
        attachment_serializer = AttatchmentSerializer(attachment, many=True)
        return Response(data=(review_serializer.data, comments_serializer.data, attachment_serializer.data))

    def put(self, request, review_id):
        # review = Review.objects.get(review_id=review_id)
        reviews = Review.objects.filter(review_id=review_id) # 임시 작동 확인용
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







