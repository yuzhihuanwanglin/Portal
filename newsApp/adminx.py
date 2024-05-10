from django.contrib import admin

# Register your models here.
import xadmin
from newsApp.models import Mynew


class MynewAdmin(object):
    """注册newsApp后台"""
    style_fields = {'description': 'ueditor'}  # 富文本编辑器的注册


xadmin.site.register(Mynew, MynewAdmin)
