from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class News(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    article = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.article