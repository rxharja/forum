from django.db import models


class Game(models.Model):
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=255)
    photo = models.ImageField()
    rating = models.FloatField()
    complexity = models.FloatField()
