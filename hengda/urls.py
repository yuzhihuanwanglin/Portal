"""hengda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import xadmin
from hengda import settings
from homeApp import views

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('', views.home, name='home'),
    path('aboutApp/', include('aboutApp.urls', namespace='aboutApp')),   # 公司简介
    path('serviceApp/', include('serviceApp.urls', namespace='serviceApp')),   # 服务支持
    path('contactApp/', include('contactApp.urls', namespace='contactApp')),  # 人才招聘
    path('newsApp/', include('newsApp.urls', namespace='newsApp')),   # 新闻动态
    path('productsApp/', include('productsApp.urls', namespace='productsApp')),   # 产品中心
    path('scienceApp/', include('scienceApp.urls', namespace='scienceApp')),   # 科研基地
    path('ueditor/', include('DjangoUeditor.urls')),   # 编辑
    path('search/', include('haystack.urls')),    # 添加haystack搜索的路径


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
