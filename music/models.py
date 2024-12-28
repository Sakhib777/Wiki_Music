from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateField()
    image = models.ImageField(upload_to='groups/')

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField()
    cover = models.ImageField(upload_to='albums/')

    def __str__(self):
        return self.name
    
class Song(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, null=True, blank=True, related_name='songs')
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    duration = models.TimeField()
    audio_file = models.FileField(upload_to='songs/')
    lyrics = models.TextField(blank=True)
    
    def __str__(self):
        return self.name
# Create your models here.
