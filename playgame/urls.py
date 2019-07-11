from django.urls import path
from django.conf.urls import url
from playgame import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^playgame/$', views.userAPI.as_view()),
    url(r'^ajax/getStones/$', views.getStones.as_view()),
]


