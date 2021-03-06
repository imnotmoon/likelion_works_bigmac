from django.db import models

# Create your models here.
class Articles(models.Model) :
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    author = models.TextField(default="guest")

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
