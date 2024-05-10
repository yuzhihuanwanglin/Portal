"""
    -*- coding: utf-8 -*-
    @Time    : 2021/4/9 15:03
    @Author  : zhongxiaoting
    @Site    : 
    @File    : forms.py
    @Software: PyCharm
"""
from django import forms
from django.utils.safestring import mark_safe

from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'sex', 'personID', 'email', 'birth', 'edu', 'school', 'major', 'experience', 'position', 'photo')

        # sex_list = (
        #     ('男', '男'),
        #     ('女', '女'),
        # )

        edu_list = (
            ('大专', '大专'),
            ('本科', '本科'),
            ('研究生', '研究生'),
            ('博士', '博士'),
            ('其它', '其它'),
        )


        widgets = {
            # 'sex': forms.Select(choices=sex_list),
            'edu': forms.Select(choices=edu_list),
            'photo': forms.FileInput(),
        }