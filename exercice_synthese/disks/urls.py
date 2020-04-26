from django.urls import path
from . import views

urlpatterns = [
    path('all-artists', views.all_artists, name='all-artists'),
    path('all-tracks', views.all_tracks, name='all-tracks'),
    path('all-albums', views.all_albums, name='all-albums'),
    path('test-base', views.test_base, name='mapage'),
    path('search', views.search, name='search'),
    path('artist/<int:id>', views.albums_from_artist, name='albums-from-artist'),
    path('album/<int:id>', views.tracks_from_albums, name='tracks-from-album'),
    path('track/<int:id>', views.track, name='track'),
]
