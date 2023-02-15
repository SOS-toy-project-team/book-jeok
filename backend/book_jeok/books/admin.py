from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Attachment

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	pass

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
	pass