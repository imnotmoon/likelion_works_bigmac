
from django.contrib import admin
from django.urls import path, include
import main.views
import article.views
import nowPlaying.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main.views.home, name="main"),
    path('nowplaying/', nowPlaying.views.nowPlaying, name="nowPlaying"),
    path('donate/', main.views.donate, name='donate'),
    path('article/', include('article.urls')),
    path('fake/', article.views.fake, name='fake')
]
