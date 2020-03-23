from django.urls import include, path,re_path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('dashboard/',views.collection,name="dashboard"),
    path('dashboard/search/',views.search,name="search"),
    path('dashboard/add/',views.search,name="add"),
    path('^dashboard/collection/', views.collection_view, name='collection_view'),
]
