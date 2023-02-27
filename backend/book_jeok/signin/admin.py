from django.contrib import admin
from .models import book_user
# Register your models here.


@admin.register(book_user)
class book_userAdmin(admin.ModelAdmin):
    pass