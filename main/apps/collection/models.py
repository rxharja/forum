from django.db import models


class Collection(models.Model):
    user_id = models.IntegerField(null=True)
    collection_name = models.CharField(max_length=255,null=True, blank=True)


class Collection_has_games(models.Model):
    user_id = models.IntegerField(null=True)
    collection_name = models.CharField(max_length=255,null=True)
    game_id = models.CharField(max_length=255,null=True, blank=True)
    game_name = models.CharField(max_length=255,null=True, blank=True)
    photo = models.CharField(max_length=1000,null=True, blank=True)
    rating = models.CharField(max_length=255, null=True, blank=True)
    difficulty = models.CharField(max_length=255, null=True, blank=True)
