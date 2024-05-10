"""
    -*- coding: utf-8 -*-
    @Time    : 2021/4/4 21:33
    @Author  : zhongxiaoting
    @Site    : 
    @File    : search_indexes.py
    @Software: PyCharm
"""
from haystack import indexes
from .models import Mynew


class MyNewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)  # document=True一般约定此字段名为text

    # 使用的模型
    def get_model(self):
        return Mynew

    # 返回的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
