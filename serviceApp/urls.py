"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/28 17:46
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from serviceApp import views

app_name = 'serviceApp'
urlpatterns = [
    path('download/', views.download, name='download'),  # 文件下载页面
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),  # 文件下载

]