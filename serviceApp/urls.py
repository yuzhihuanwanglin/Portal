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
    path('download/', views.download, name='download'),  # 资料下载页面
    path('getDoc/<int:id>/', views.getDoc, name='getDoc'),  # 资料下载
    path('facedetect/', views.facedetect, name='facedetect'),  # 本地人脸检测api
    path('platform/', views.platform, name='platform'),  # 人脸识别开放平台
    path('facedetectDemo/', views.facedetectDemo, name='facedetectDemo'),  #网络api人脸检测

]