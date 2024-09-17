from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.

def index(request):
    return render(request, 'index.html')



def weapons(request):
    return render(request, 'information.html')


def news(request):
    news = News.objects.all()
    data = {'news': news}
    return render(request, 'danie.html', data)

def post(request):
    posts = Post.objects.all()
    data = {'posts': posts}
    return render(request, '4to.html', data)


