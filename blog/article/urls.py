from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article, name="articles"),
    path('write/', views.write, name='write'),
    path('create/', views.create, name='create'),
    path('<int:article_id>/detail/', views.detail, name='detail'),
    path('<int:article_id>/delete/', views.delete, name='delete'),
    path('<int:article_id>/update/', views.update, name='update'),
]
