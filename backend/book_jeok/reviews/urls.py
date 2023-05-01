from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ReviewSimple.as_view()),
    path("user/<int:user_id>", views.ReviewByUser.as_view()),
    path("<int:review_id>", views.ReviewById.as_view()),
    # path("comments/<int:review_id>",views.CommentByReviewId.as_view())
    path("<int:review_id>/comments", views.CommentByReviewId.as_view())
]