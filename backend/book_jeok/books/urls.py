from django.urls import path
from . import views

urlpatterns = [
    # path("", views.BookViewSet.as_view(
    #         {
    #             "get": "list",
    #             "post": "create",
    #         }
    #     ),
    # ),
    # path("<int:pk>", views.BookViewSet.as_view(
    #         {
    #             "get": "retrieve",
    #             "put": "partial_update",
    #             "delete": "destroy",
    #         }
    #     ),
    # ),
    path("", views.BookSearch.as_view()),
]