from django.contrib import admin
from .models import Post, Comment
from accounts.models import Profile
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('body',)
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']



@admin.register(Profile)
class MyProfile(SummernoteModelAdmin):
    summernote_fields = ('bio',)


