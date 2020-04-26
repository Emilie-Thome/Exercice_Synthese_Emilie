from django.db import models


class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="artist's name")

    class Meta:
        verbose_name = "artist"
        db_table = 'disks_artist'

    def __str__(self):
        return self.name

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, verbose_name="album's title")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "album"
        db_table = 'disks_album'

    def __str__(self):
        return self.title

class Track(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name="track's title")
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    composer = models.CharField(max_length=200, verbose_name="composer")
    milliseconds = models.TextField(verbose_name="track's duration")
    bytes = models.IntegerField()
    unitprice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="price")

    class Meta:
        verbose_name = "track"
        db_table = 'disks_track'

    def __str__(self):
        return self.name
