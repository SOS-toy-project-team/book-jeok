from django.urls import path
from . import views
from .views import SignUpView, LoginView, LogoutView

urlpatterns = [
    path('', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
]