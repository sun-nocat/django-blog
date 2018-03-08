from django.contrib import admin

# Register your models here.
from todolist import models
admin.site.register(models.Todo)