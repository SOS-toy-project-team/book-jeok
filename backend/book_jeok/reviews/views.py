from django.shortcuts import render
from rest_framework import status

from signin.models import book_user
from .models import Review, Comment
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewSerializer, CommentSerializer, ReviewSerializerSave, CommentSerializerSave
from books.serializers import BookSerializer, BookSerializerSave


class ReviewSimple(APIView):
    """모든 리뷰들을 보내줌"""

    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request):
        # 책 저장 로직
        book_serializer = BookSerializerSave(data=request.data)

        if not book_serializer.is_valid():
            return Response(book_serializer.errors(), status=status.HTTP_400_BAD_REQUEST)

        book_serializer.save()

        # 리뷰 저장 로직
        request.data['book_id'] = book_serializer.data.get('book_id') # request.data에 위에서 저장된 book_id를 추가
        review_serializer = ReviewSerializerSave(data=request.data) # request.data를 직력화시켜줌

        if not review_serializer.is_valid():
            return Response(review_serializer.errors(), status=status.HTTP_400_BAD_REQUEST)

        review_serializer.save()

        return Response((review_serializer.data, book_serializer.data), status=status.HTTP_201_CREATED)


class ReviewById(APIView):
    """review_id에 해당하는 게시글 관련 클래스"""

    def get(self, request, review_id):
        review = Review.objects.filter(review_id=review_id)
        serializer = ReviewSerializer(review, many=True)
        print(serializer.data)
        return Response(data=serializer.data)

    def put(self, request, review_id):
        review = Review.objects.get(review_id=review_id)
        serializer = ReviewSerializerSave(review, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, review_id):
        review = Review.objects.get(review_id=review_id)
        review.delete()
        return Response(status=status.HTTP_200_OK)


class ReviewByUser(APIView):
    """ user_id에 해당하는 게시글들을 보내줌 """

    def get(self, request, user_id):
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class CommentByReviewId(APIView):
    """review_id를 받아서 댓글 조회 및 작성"""

    def get(self, request, review_id):
        comments = Comment.objects.filter(review_id=review_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)

    def post(self, request, review_id):
        request.data["review_id"] = review_id
        serializer = CommentSerializerSave(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors(), status=status.HTTP_400_BAD_REQUEST)


class CommentById(APIView):
    """comment_id를 받아서 댓글 조회,수정 및 삭제"""

    def get(self, request, comment_id):
        comments = Comment.objects.select_related('user_id').filter(comment_id=comment_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(data=serializer.data)

    def put(self, request, comment_id):
        comment = Comment.objects.get(comment_id=comment_id)
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        comment = Comment.objects.get(comment_id=comment_id)
        comment.delete()
        return Response(status=status.HTTP_200_OK)
