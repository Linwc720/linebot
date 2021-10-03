from django.contrib import admin

# Register your models here.
from jobebot.models import *

class User_Info_Admin(admin.ModelAdmin):
    list_display = ('id','uid','name','pic_url','mtext','notify','mdt')
admin.site.register(User_Info,User_Info_Admin)