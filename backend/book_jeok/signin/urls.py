from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view()),
]