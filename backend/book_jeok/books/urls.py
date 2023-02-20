from django.urls import path
from . import views
from .views import api_book_search

urlpatterns = [
    path("", views.BookViewSet.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path("<int:pk>", views.BookViewSet.as_view(
            {
                "get": "retrieve",
                "put": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path("api_book_search", api_book_search),
]