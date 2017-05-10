from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author']
    list_display_links = ['title']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

