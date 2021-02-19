from django.db import models

# Create your models here.

class News(models.Model):
    article = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.article