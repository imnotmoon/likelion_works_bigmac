from django.contrib import admin
from article.models import Articles
from main.models import Movies

# Register your models here.
admin.site.register(Articles)
admin.site.register(Movies)