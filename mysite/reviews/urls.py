from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>/', views.detail, name='detail'),
    path('<int:course_id>/results/', views.results, name='results'),
    path('<int:course_id>/review/', views.review, name='review'),
]
