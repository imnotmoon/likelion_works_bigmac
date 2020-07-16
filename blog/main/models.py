from django.db import models

# Create your models here.
class Movies(models.Model) :
    title = models.CharField(max_length=20)
    grade = models.IntegerField(default=0)
    postdate = models.CharField(max_length=20, null=True)
    subDescription = models.CharField(max_length=50, null=True)
    poster = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

    