"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/28 17:46
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from contactApp import views

app_name = 'contactApp'
urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('recruit/', views.recruit, name='recruit'),

]