"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/28 17:46
    @Author  : zhongxiaoting
    @Site    : 
    @File    : urls.py
    @Software: PyCharm
"""
from django.urls import path

from aboutApp import views

app_name = 'aboutApp'
urlpatterns = [
    path('survey/', views.survey, name='survey'),
    path('honor/', views.honor, name='honor'),
    path('service_terms/', views.service_terms, name='service_terms'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),


]
