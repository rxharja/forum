from django.db import models


class Recommended(models.Model):
    user_id = models.FloatField(null=True)
    name = models.CharField(max_length=255,null=True, blank=True)
    # genre = models.CharField(max_length=255,null=True, blank=True)
    # photo = models.ImageField(upload_to='public/media/',null=True, blank=True)
    rating = models.CharField(max_length=255, null=True, blank=True)
    difficulty = models.CharField(max_length=255, null=True, blank=True)

    # @property
    # def get_photo(self):
    #     if self.photo and hasattr(self.photo, 'url'):
    #         return self.photo.url
    #     else:
    #         return '/public/media/default.png'

    # def __str__(self):
    #     return self.photo.url
