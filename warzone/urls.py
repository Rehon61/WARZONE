"""
URL configuration for warzone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from news_warzone import views as main


urlpatterns = [
    path('', main.index), # Главная страница
    path('weapons/', main.weapons, name='weapons'),# сборка оружий в Warzone
    path('news/', main.news, name='news'), # новости типо
    path('post/', main.post, name='post'), # новости типо

]
