from django.shortcuts import render, get_object_or_404
import markdown
import re
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
# Create your views here.
from blog.models import Post, Category, Tag


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={
        'post_list': post_list
    })


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # 先实例化了一个 markdown.Markdown 对象 md，和 markdown.markdown() 方法一样，也传入了 extensions 参数。
    # 接着我们便使用该实例的 convert 方法将 post.body 中的 Markdown 文本解析成 HTML 文本。
    # 而一旦调用该方法后，实例 md 就会多出一个 toc 属性，这个属性的值就是内容的目录，我们把 md.toc 的值赋给 post.toc 属性
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',  # 基础拓展
        'markdown.extensions.codehilite',  # 语法高亮拓展
        'markdown.extensions.toc',  # 允许自动生成目录
        TocExtension(slugify=slugify),
    ])

    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request, 'blog/detail.html', context={'post': post})


# 归档页面
def archive(request, year, month):
    # Python 中调用属性的方式通常是 created_time.year，但是由于这里作为方法的参数列表，所以 django 要求我们把点替换成了两个下划线，即 created_time__year。
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month,
                                    ).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 分类页面
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})


# 标签页面
def tag(request, pk):
    t = get_object_or_404(Tag, pk=pk)
    post_list = Post.objects.filter(tags=t).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
