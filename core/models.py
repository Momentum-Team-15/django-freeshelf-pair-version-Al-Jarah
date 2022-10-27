from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils import timezone
# Create your models here.


class User(AbstractUser):
    pass


class Resource(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey("Category", blank=True, null=True, on_delete=models.CASCADE, related_name="resources")

    def __str__(self):
        return f"{self.title} by {self.author}"


class Favorite(models.Model):
    resource = models.ForeignKey('Resource', on_delete=models.CASCADE, blank=True, related_name="favorites")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name
