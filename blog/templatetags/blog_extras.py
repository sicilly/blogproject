from django import template

from ..models import Post, Category, Tag
# 这里我们首先导入 template 这个模块，然后实例化了一个 template.Library 类，并将函数 show_recent_posts 装饰为 register.inclusion_tag，
# 这样就告诉 django，这个函数是我们自定义的一个类型为 inclusion_tag 的模板标签。
register = template.Library()


# 最新文章模板标签
# inclusion_tag 模板标签和视图函数的功能类似，它返回一个字典值，字典中的值将作为模板变量，传入由 inclusion_tag 装饰器第一个参数指定的模板。
# 当我们在模板中通过 {% show_recent_posts %}使用自己定义的模板标签时，django 会将指定模板的内容使用模板标签返回的模板变量渲染后替换。
@register.inclusion_tag('blog/inclusions/_recent_posts.html', takes_context=True)
def show_recent_posts(context, num=5):
    return {
        'recent_post_list': Post.objects.all().order_by('-created_time')[:num]
    }


# 归档模板标签
@register.inclusion_tag('blog/inclusions/_archives.html', takes_context=True)
def show_archives(context):
    return {
        'date_list': Post.objects.dates('created_time', 'month', order='DESC')
    }


# 分类模板标签
@register.inclusion_tag('blog/inclusions/_categories.html', takes_context=True)
def show_categories(context):
    return {
        'category_list': Category.objects.all(),
    }


# 标签云模板标签
@register.inclusion_tag('blog/inclusions/_tags.html', takes_context=True)
def show_tags(context):
    return {
        'tag_list': Tag.objects.all()
    }