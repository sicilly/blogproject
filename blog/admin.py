from django.contrib import admin
from .models import Post, Category, Tag
# Register your models here.


# 定义了一个 PostAdmin 来配置 Post 在 admin 后台的一些展现形式。list_display 属性控制 Post 列表页展示的字段。此外还有一个 fields 属性，则用来控制表单展现的字段
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']

    # Postadmin 继承自 ModelAdmin，它有一个 save_model 方法，
    # 这个方法只有一行代码：obj.save()。它的作用就是将此 Modeladmin 关联注册的 model 实例（这里 Modeladmin 关联注册的是 Post）保存到数据库。
    def save_model(self, request, obj, form, change):
        obj.author = request.user  # 通过 request.user 取到当前请求用户,将其关联到新创建的文章
        super().save_model(request, obj, form, change)


# 要在后台注册我们自己创建的几个模型，这样 django admin 才能知道它们的存在
# 把新增的 Postadmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)