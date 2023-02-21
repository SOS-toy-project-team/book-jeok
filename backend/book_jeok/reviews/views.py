from django.shortcuts import render
from rest_framework import status

from .models import Review, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewSerializer, CommentSerializer, ReviewSerializerSave, CommentSerializerSave
from books.serializers import BookSerializer

class ReviewSimple(APIView):

    """모든 리뷰들을 보내줌"""
    def get(self, request):
        all_review = Review.objects.select_related('book_id', 'user_id')
        serializer = ReviewSerializer(all_review, many=True)
        return Response(serializer.data)

    """ request data에 user_id, book_id가 담겨 와야함"""
    def post(self, request):
        # 책 저장 로직
        book_data = {'title': request.data.get('title'), 'publisher': request.data.get('publisher'),
                     'author': request.data.get('author'), 'description': request.data.get('description'),
                     'pubdate': request.data.get('pubdate'), 'path': request.data.get('path')}

        book_serializer = BookSerializer(data=book_data)

        if not book_serializer.is_valid():
            return Response(book_serializer.errors(), status=status.HTTP_400_BAD_REQUEST)

        book_serializer.save()

        # 리뷰 저장 로직
        review_data = {'book_id': book_serializer.data.get('book_id'), 'user_id': request.data.get('user_id'), 'content': request.data.get('content'),
                       'star_point': request.data.get('star_point')}

        review_serializer = ReviewSerializerSave(data=review_data)

        if not review_serializer.is_valid():
            return Response(review_serializer.errors(), status=status.HTTP_400_BAD_REQUEST)

        review_serializer.save()

        return Response((review_serializer.data, book_serializer.data), status=status.HTTP_201_CREATED)

class ReviewByUser(APIView):
    """ user_id에 해당하는 게시글들을 보내줌 """
    def get(self, request, user_id):
        reviews = Review.objects.select_related('book_id', 'user_id').filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewById(APIView):
    """review_id에 해당하는 게시글 관련 클래스"""
    def get(self, request, review_id):
        review = Review.objects.filter(review_id=review_id)
        print(review.values())
        review_serializer = ReviewSerializer(review, many=True)

        return Response(data=review_serializer.data)

    # def put(self, request, review_id):
    #     # review = Review.objects.get(review_id=review_id)
    #     reviews = Review.objects.filter(review_id=review_id) # 임시 작동 확인용
    #     serializer = ReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentById(APIView):
    """review_id를 받아서 댓글 CRUD 구현"""
    def get(self, request, review_id):
        comments = Comment.objects.select_related('user_id').filter(review_id=review_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)

    def post(self, request, review_id):

        comment_data = {'user_id': request.data.get('user_id'), 'review_id': request.data.get('review_id'), 'content': request.data.get('content')}

        serializer = CommentSerializerSave(data=comment_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors(), status=status.HTTP_400_BAD_REQUEST)













