from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('artist/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('album/<int:pk>/', views.album_detail, name='album_detail'),
    path('song/<int:pk>/', views.song_detail, name='song_detail'),
    path('search/', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)