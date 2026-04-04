from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('notes/<int:note_id>', views.detail, name='detail'),
    path('register/', views.register, name='register')
]