from django.db import models
from django.core.validators import URLValidator
from django.conf import settings


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    thumbnail = models.CharField(max_length=255, validators=[URLValidator])
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
