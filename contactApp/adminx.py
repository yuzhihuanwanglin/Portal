from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

import xadmin
from contactApp.models import Ad, Resume


class AdAdmin(object):
    list_display = ('id', 'title', 'description', 'publish_date')

    fields = ('title', 'description', 'publish_date')


xadmin.site.register(Ad, AdAdmin)


class ResumeAdmin(object):
    list_display = ('name', 'status', 'email', 'edu', 'school', 'major', 'position', 'publish_data', 'image_data')

    def image_data(self, obj):
        return mark_safe(u'<img src="%s" width="120px"/>' % obj.photo.url)

    image_data.short_description = u'个人照片'


xadmin.site.register(Resume, ResumeAdmin)
