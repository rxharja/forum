from django.contrib import admin
from .models import Collection, Collection_has_games


class CollectionAdmin(admin.ModelAdmin):
    list_display = ['user_id','collection_name',]


class CollectionHasGamesAdmin(admin.ModelAdmin):
    list_display = ['user_id','collection_name','game_id','photo','rating', 'difficulty',]


admin.site.register(Collection , CollectionAdmin)
admin.site.register(Collection_has_games, CollectionHasGamesAdmin)
