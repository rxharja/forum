from django.db import models


class Game(models.Model):
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='public/media/',null=True, blank=True)
    rating = models.FloatField(null=True)
    complexity = models.FloatField(null=True)

    @property
    def get_photo(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return '/public/media/default.png'

    def __str__(self):
        return self.photo.url
