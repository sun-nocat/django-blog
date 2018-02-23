from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
from .models import Post, Category

# Create your views here.
#Web 服务器的作用就是接收来自用户的 HTTP 请求，根据请求内容作出相应的处理，并把处理结果包装成 HTTP 响应返回给用户。
#request 就是 Django 为我们封装好的 HTTP 请求
def index(request):
    post_list= Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

    # return render(request,'blog/index.html',context={
    #     'title':'我的博客首页',
    #     'welcome':'欢迎访问我的博客'
    # })
#首先把 HTTP 请求传了进去，然后 render 根据第二个参数的值 blog/index.html 找到这个模板文件并读取模板中的内容
#render 根据我们传入的 context 参数的值把模板中的变量替换为我们传递的变量的值

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/detail.html', context={'post': post})
def archives(request, year, month):
    post_list = Post.objects.filter(created_time__year=year,
                                    created_time__month=month
                                    )
    return render(request, 'blog/index.html', context={'post_list': post_list})
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/index.html', context={'post_list': post_list})

# class IndexView(ListView):
#     model = Post
#     template_name = 'blog/index.html'
#     context_object_name = 'post_list'
#     # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
#     paginate_by = 10







