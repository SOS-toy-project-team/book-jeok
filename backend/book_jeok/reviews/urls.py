from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.ReviewSimple.as_view()),
    path("user/<int:user_id>", views.ReviewUser.as_view()),
]