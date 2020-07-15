from django.db import models

# Create your models here.
class Movies(models.Model) :
    title = models.CharField(max_length=20)
    grade = models.IntegerField()
    postdate = models.CharField(max_length=30)
    subDescription = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    