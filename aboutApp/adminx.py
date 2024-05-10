from django.contrib import admin

# Register your models here.
import xadmin
from aboutApp.models import Award


class AwardAdmin(object):
    """xadmin后台注册"""
    list_display = ['id', 'description', 'photo']
    fields = ['description', 'photo']


xadmin.site.register(Award, AwardAdmin)
