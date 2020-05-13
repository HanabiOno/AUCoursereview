from django.urls import path

from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #results page is not necessary if we want to show the reviews on the index page of the course already
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:course_id>/review/', views.review, name='review'),
]
