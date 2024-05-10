from django.shortcuts import render


# Create your views here.

def science(request):
    return render(request, 'scienceApp/science.html')
