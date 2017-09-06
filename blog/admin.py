from django.contrib import admin
from .models import Posts, Comments
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'pub_date', 'post_title', 'post_text')

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'pub_date', 'comment')

admin.site.register(Posts, PostsAdmin)
admin.site.register(Comments, CommentsAdmin)