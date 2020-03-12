from django.contrib import admin
from .models import Game


class GameAdmin(admin.ModelAdmin):
    list_display = ('description', 'genera', 'photo')


admin.site.register(Game , GameAdmin)
