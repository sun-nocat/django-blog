import json

from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
# Create your views here.
from todolist import models

#页面
#显示输入页面，从数据库中拿出所有的值
#返回值user_list. 返回经过渲染的页面
def home(req):
#    user_list=models.Todo.objects.all()
    return render(req,'todolist.html')



#接口
#增加username和todo的内容，从前端取到数据，然后同步数据库
#返回参数user_list  返回json的字典数据
#增加信息，并返回页面
def api_add_todo(request):
    if request.method=="POST":
        t = request.POST.get("todo", None)
        print(t)
       # u = request.POST.get("tag", None)
#        e = request.POST.get("flag",)
        models.Todo.objects.create(         #更新数据库
            flag=1,
            tag=0,
            todo=t,
        )
        all_todo= models.Todo.objects.all()
      #  return render(request,'index.html',{'all_todo':all_todo})
    #user_list=serializers.serialize("json",models.Todo.objects.all())
    #return HttpResponse(json.dumps(user_list),content_type="application/json")
    return HttpResponse("{'sqkr':13}",content_type="application/json")




#接口
#删除，根据username来删除数据库中相关的数据，并返回表中的所有值。
#返回值：todo_list  json的字典格式
def api_delete_todo(request):#根据user删除信息
    #onetodo=''
    if request.method=="POST":

        #user_list=[]
        onetodo = request.POST.get('todo',None)
        models.Todo.objects.filter(todo=onetodo).delete()

    #all_todo = models.Todo.objects.all()
    #todo_list = serializers.serialize("json",models.Todo.objects.all())
   # return render(request, 'index.html',{'all_todo':all_todo})
    return HttpResponse("{'sqkr':13}",content_type="application/json")
# {
#     status: 0,
#     msg: "aasddsasd",
#     data: {
#
#     }
# }
# {
#     toda:asd
# }

#接口
#返回所有值
#返回值：all_list
def api_all_todo(request):
    all_list=serializers.serialize("json", models.Todo.objects.all())

    return HttpResponse(all_list,content_type="application/json")


#接口
#接受前端的点击事件，使数据库中的flag变为0
#返回值，返回数据库中所有的值
def api_flag1_todo(request):
    if request.method == "POST":
       # flag1 = request.POST.get("flag")

        name = request.POST.get("todo",None)
        models.Todo.objects.filter(todo=name).update(flag=1)
    all_todo = models.Todo.objects.all()
   # return render(request, 'index.html',{'all_todo':all_todo})

    #all_list=serializers.serialize("json",models.Todo.objects.all())
    #return HttpResponse(json.dumps(all_list),content_type="application/json")
    return HttpResponse("{'sqkr':13}",content_type="application/json")

def api_flag0_todo(request):
    if request.method == "POST":
       # flag1 = request.POST.get("flag")

        name = request.POST.get("todo",None)
        models.Todo.objects.filter(todo=name).update(flag=0)
    #all_todo = models.Todo.objects.all()
   # return render(request, 'index.html',{'all_todo':all_todo})

    #all_list=serializers.serialize("json",models.Todo.objects.all())
    #return HttpResponse(json.dumps(all_list),content_type="application/json")
    return HttpResponse("{'sqkr':13}",content_type="application/json")





#接口
#接受前端的点击事件，是数据库中的p



# riority从0变为1，如果本来是1，那么就变成0
#返回值，返回数据可中的所有值
def api_tag_todo(request):
    if request.method == "POST":
        todo1 = request.POST.get("todo",None)
        tag1 = request.POST.get("tag")
        models.Todo.objects.filter(todo=todo1).update(tag=tag1)
    all_todo = models.Todo.objects.all()

    #all_todo=serializers.serialize("json",models.Todo.objects.all())
    return render(request, 'index.html',{'all_todo':all_todo})
    #return HttpResponse(json.dumps(all_list),content_type="application/json")















