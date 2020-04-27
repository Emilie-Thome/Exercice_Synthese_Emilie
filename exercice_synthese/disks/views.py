from django.shortcuts import render, get_object_or_404
from disks.models import Artist, Album, Track



def home(request):
    """ Test the base.html """
    return render(request, 'disks/home.html',)

def search(request):
    """ Search page """
    id_artist = request.GET.get('query-artist', '')
    if id_artist != '':
        the_artist = Artist.objects.filter(id=id_artist)
        return render(request, 'disks/all-artists.html', {'all_artists': the_artist})

    id_album = request.GET.get('query-album', '')
    if id_album != '':
        the_album = Album.objects.filter(id=id_album)
        return render(request, 'disks/all-albums.html', {'all_albums': the_album})

    id_track = request.GET.get('query-track', '')
    if id_track != '':
        the_track = get_object_or_404(Track, id=id_track)
        return render(request, 'disks/track.html', {'track': the_track})

    artists = Artist.objects.all()
    albums = Album.objects.all()
    tracks = Track.objects.all()
    return render(request, 'disks/search.html', {'all_artists': artists,
                                                   'all_albums': albums,
                                                   'all_tracks': tracks})


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
    albums = Album.objects.filter(artist = the_artist)
    return render(request, 'disks/all-albums.html', {'all_albums': albums})

def tracks_from_albums(request, id):
    """ View all tracks from an album """
    the_album = get_object_or_404(Album, id=id)
    tracks = Track.objects.filter(album=the_album)
    return render(request, 'disks/all-tracks.html', {'all_tracks': tracks})

def track(request, id):
    """ View all tracks from an album """
    the_track = get_object_or_404(Track, id=id)
    return render(request, 'disks/track.html', {'track': the_track})