from django.shortcuts import render
from disks.models import Artist



def all_artists(request):
    """ View all artists of the DB """
    artists = Artist.objects.all()
    return render(request, 'disks/all-artists.html', {'all_artists': artists})