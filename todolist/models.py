from django.db import models
from django.urls import reverse

# Create your models here.
'''
class UserInfo(models.Model):
    username = models.CharField(max_length=64)
    sex = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
'''
class Todo(models.Model):
#    username = models.CharField(max_length=64)
    todo = models.CharField(max_length=100)
    flag = models.CharField(max_length=2)#是否完成
#    priority = models.CharField(max_length=2,default='0')
    tag = models.CharField(max_length=10, null=True)#标签
    creattime = models.DateTimeField(auto_now_add=True)
