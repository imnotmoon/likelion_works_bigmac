from django.db import models

# Create your models here.
class Sets(models.Model) :
    title = models.CharField(max_length=20, null=False)
    name = models.CharField(max_length=20, null=False)
    cover = models.CharField(max_length=40, default="")
    genre = models.IntegerField(null=False, default=1)

    def __str__(self) :
        return self.title

