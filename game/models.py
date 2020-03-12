from django.db import models


class Game(models.Model):
    description = models.CharField(max_length=1000)
    genera = models.CharField(max_length=255)
    photo = models.ImageField()
