from django.contrib import admin
from .models import Recommended


class RecommendedAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'name', 'difficulty','rating')


admin.site.register(Recommended , RecommendedAdmin)
