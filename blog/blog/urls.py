
from django.contrib import admin
from django.urls import path
import main.views
import article.views
import nowPlaying.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="main"),
    path('articles/', article.views.article, name="articles"),
    path('nowplaying/', nowPlaying.views.nowPlaying, name="nowPlaying"),
    path('article/write/', article.views.write, name='write'),
    path('article/create/', article.views.create, name='create'),
    path('article/<int:article_id>/detail/', article.views.detail, name='detail'),
    path('article/<int:article_id>/delete/', article.views.delete, name='delete'),
    path('article/<int:article_id>/update/', article.views.update, name='update'),
    path('donate/', main.views.donate, name='donate')
]
