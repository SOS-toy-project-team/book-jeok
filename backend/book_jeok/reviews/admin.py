from django.contrib import admin
from .models import Review,Comment, User


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class CommentAdmin(admin.ModelAdmin):
    pass
