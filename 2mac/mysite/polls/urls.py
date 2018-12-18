from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('read/<int:key>/', views.read, name='read'),
    path('create', views.create, name='create'),
    path('update/<int:key>/', views.update, name='update'),
    path('delete/<int:key>/', views.delete, name='delete'),
]