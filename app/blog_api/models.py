from django.db import models
from django.core.validators import URLValidator
from django.conf import settings


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=46, unique=True)

    def __str__(self):
        return f"{self.name}"


class Article(models.Model):
    title = models.CharField(max_length=60, unique=True)
    thumbnail = models.URLField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.title}"
