"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/28 17:46
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from newsApp import views

app_name = 'newsApp'
urlpatterns = [
    path('news/<str:newsName>/', views.news, name='news'),
    path('newDetail/<int:id>/', views.details, name='newDetail'),
]