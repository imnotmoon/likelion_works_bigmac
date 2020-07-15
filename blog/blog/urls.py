
from django.contrib import admin
from django.urls import path
import main.views
import article.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="main"),
    path('articles/', article.views.article, name="articles")
]
