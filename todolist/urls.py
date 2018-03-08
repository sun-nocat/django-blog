from django.conf.urls import url
from . import views
#我们首先从 django.conf.urls 导入了 url 函数，又从当前目录下导入了 views 模块。然后我们把网址和处理函数的关系写在了 urlpatterns 列表里

app_name='todolist'
urlpatterns=[
#第一个参数是网址，第二个参数是处理函数），另外我们还传递了另外一个参数 name，这个参数的值将作为处理函数 index 的别名
    url(r'^home', views.home),
    url(r'^api_add_todo', views.api_add_todo),
    url(r'^api_delete_todo', views.api_delete_todo),
    url(r'^api_all_todo', views.api_all_todo),
    url(r'^api_flag1_todo', views.api_flag1_todo),
    url(r'^api_flag0_todo', views.api_flag0_todo),

    url(r'^api_tag_todo', views.api_tag_todo),
#以 post/ 开头，后跟一个至少一位数的数字，并且以 / 符号结尾，如 post/1/
]