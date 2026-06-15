from django.urls import path
from . import views

app_name = 'museum_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schedule/', views.schedule, name='schedule'),
    path('news/', views.news_list, name='news_list'),
    path('news/<slug:slug>/', views.news_detail, name='news_detail'),
    path('contacts/', views.contacts, name='contacts'),
    path('excursion/', views.excursion_request, name='excursion_request'),
    path('excursion/confirm/<str:token>/', views.confirm_excursion, name='confirm_excursion'),
    path('virtual-tour/', views.virtual_tour, name='virtual_tour'),
    path('quiz/', views.quiz, name='quiz'),
]