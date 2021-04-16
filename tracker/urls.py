from django.urls import path, re_path

from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home),
    path('map/', views.map, name="map"),
    path('sightings/', views.SightingListView.as_view(), name="sighting-list"),
    # path('sightings/<str:id>/', views.update),
    re_path(r'sightings/(?P<squirrel_id>\d{1,2}[A-Z]{1}-[A-Z]{2}-\d{4}-\d{2})', views.update, name='update'),
    path('sightings/add/', views.add, name="add"),
    path('sightings/stats/', views.stat, name="stat"),
]

