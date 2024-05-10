from django.contrib import admin

# Register your models here.
import xadmin
from serviceApp.models import Doc


class DocAdmin(object):
    list_display = ('title', 'file', 'publish_date')
    field = ('title', 'file', 'publish_date')


xadmin.site.register(Doc, DocAdmin)
