from django.urls import include, path
from . import views


urlpatterns = [
    path('recommendations',views.games,name="Recommendations"),
]
