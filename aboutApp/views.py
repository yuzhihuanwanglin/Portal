from django.shortcuts import render


# Create your views here.
# 企业概况
from aboutApp.models import Award


def survey(request):
    return render(request, 'aboutApp/survey.html', {'active_menu': 'about', 'sub_menu': 'survey'})


# 荣誉资质
def honor(request):
    awards = Award.objects.all()
    context = {
        'awards': awards,
        'active_menu': 'about',
        'sub_menu': 'honor'
    }
    return render(request, 'aboutApp/honor.html', context)
