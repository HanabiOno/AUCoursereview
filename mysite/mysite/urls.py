"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from polls.views import home_view, HUM_view, SCI_view, SSC_view, ACC_view

urlpatterns = [
    path('', home_view, name = 'home'),
    path('HUM', HUM_view, name = 'HUM'),
    path('SCI', SCI_view, name = 'SCI'),
    path('SSC', SSC_view, name = 'SSC'),
    path('ACC', ACC_view, name = 'ACC'),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
