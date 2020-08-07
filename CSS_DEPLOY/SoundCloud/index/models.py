from django.db import models

# Create your models here.
class Playlist(models.Model) :
    title = models.CharField(max_length=200, default="title")
    name = models.CharField(max_length=200, default="bigmac")
    # 1 : chill / 2 : party / 3 : relax / 4 : study / 5 : workout
    mood = models.IntegerField(null=False, default=1)
    image = models.CharField(max_length=400, null=True)

    def __str__(self) :
        return self.title