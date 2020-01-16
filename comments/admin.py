from django.contrib import admin
from .models import Comment
# Register your models here.


# 注册评论模型到 admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'url', 'post', 'created_time']
    fields = ['name', 'email', 'text', 'post']


admin.site.register(Comment, CommentAdmin)