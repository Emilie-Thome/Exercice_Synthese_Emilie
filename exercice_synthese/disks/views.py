from django.shortcuts import render, get_object_or_404
from disks.models import Artist, Album, Track


def research(request):
    """ Research page """
    artists = Artist.objects.all()
    albums = Album.objects.all()
    tracks = Track.objects.all()
    return render(request, 'disks/research.html', {'all_artists': artists,
                                                   'all_albums': albums,
                                                   'all_tracks': tracks})


def test_base(request):
    """ Test the base.html """
    return render(request, 'disks/mapage.html',)

def all_artists(request):
    """ View all artists of the DB """
    artists = Artist.objects.all()
    return render(request, 'disks/all-artists.html', {'all_artists': artists})
def all_albums(request):
    """ View all albums of the DB """
    albums = Album.objects.all()
    return render(request, 'disks/all-albums.html', {'all_albums': albums})
def all_tracks(request):
    """ View all tracks of the DB """
    tracks = Track.objects.all()
    return render(request, 'disks/all-tracks.html', {'all_tracks': tracks})

def albums_from_artist(request, id):
    """ View all albums from an artist """
    the_artist = get_object_or_404(Artist, id=id)
    albums = Album.objects.get(artist = the_artist)
    return render(request, 'disks/all-albums.html', {'all_albums': albums})