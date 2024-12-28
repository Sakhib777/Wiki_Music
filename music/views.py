from django.shortcuts import render, get_object_or_404
from .models import Artist, Album, Song

# Главная страница
def home(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    songs = Song.objects.all()
    return render(request, 'home.html', {
        'artists': artists,
        'albums': albums,
        'songs': songs,
    })

# Детальная страница для Artist
def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'artist_detail.html', {'artist': artist})

# Детальная страница для Album
def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'album': album})

# Детальная страница для Song
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'song_detail.html', {'song': song})

# Поисковик
def search(request):
    query = request.GET.get('q')
    artists = Artist.objects.filter(name__icontains=query)
    albums = Album.objects.filter(name__icontains=query)
    songs = Song.objects.filter(name__icontains=query)
    return render(request, 'search.html', {
        'query': query,
        'artists': artists,
        'albums': albums,
        'songs': songs,
    })
