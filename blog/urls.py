from django.urls import path

from . import views

"""
绑定关系的写法是把网址和对应的处理函数作为参数传给 path 函数（第一个参数是网址，第二个参数是处理函数），另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名，这在以后会用到
"""
# 告诉 django 这个 urls.py 模块是属于 blog 应用的，这种技术叫做视图函数命名空间。
app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.detail, name='detail'),
    path('archives/<int:year>/<int:month>/', views.archive, name='archive'),
    path('categories/<int:pk>/', views.category, name='category'),
    path('tags/<int:pk>/', views.tag, name='tag'),
]
