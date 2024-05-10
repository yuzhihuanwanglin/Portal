from django.core.paginator import Paginator
from django.shortcuts import render
from pyquery import PyQuery as pq
# Create your views here.
from newsApp.models import Mynew


def news(request, newsName):
    """新闻动态的动态选择"""
    submenu = newsName
    if newsName == 'company':
        newsName = "企业要闻"
    elif newsName == 'industry':
        newsName = '行业新闻'
    else:
        newsName = '通知公告'

    # 从数据库中取出数据
    new_list = Mynew.objects.filter(newType=newsName).order_by('-publish_date')
    # 对每条数据进行<p>的文本抽取
    for mynew in new_list:
        html = pq(mynew.description)  # 利用pq解析html内容
        mynew.mytxt = pq(html)('p').text()  # 截取html的文字

    # 分页处理
    p = Paginator(new_list, 4)
    # 获取当前页数
    page = int(request.GET.get('page', 1))
    # 根据当前页码，返回数据
    news_list = p.page(page)

    context = {
        'active_menu': 'news',
        'sub_menu': submenu,
        'newList': news_list,
        'newName': newsName
    }

    return render(request, 'newsApp/newsList.html', context)


def details(request, id):
    mynew = Mynew.objects.get(id=id)
    mynew.views += 1
    mynew.save()
    context = {
        'active_menu': 'news',
        'mynew': mynew,
    }
    return render(request, 'newsApp/newsDetails.html', context)





