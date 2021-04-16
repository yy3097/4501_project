from django.urls import path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home),
    path('map/', views.map, name="map"),
    path('sightings/', views.SightingListView.as_view(), name="sighting-list"),
]

