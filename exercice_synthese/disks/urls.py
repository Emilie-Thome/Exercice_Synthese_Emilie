from django.urls import path
from . import views

urlpatterns = [
    path('all-artists', views.all_artists, name='all-artists'),
]
