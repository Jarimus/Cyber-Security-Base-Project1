from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='Index'),
    path('ping', views.PingView, name='Ping!'),
    path('test/routing', views.TestView),
]