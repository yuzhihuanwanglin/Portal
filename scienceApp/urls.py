"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/28 17:46
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from scienceApp import views

app_name = 'scienceApp'
urlpatterns = [
    path('science/', views.science, name='science')

]