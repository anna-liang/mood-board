from django.shortcuts import render

from .apps import spotifyObj

from .models import MoodBlock

# Create your views here.
def index(request):
    uniqueAlbums = []
    topTracks = []
    results = spotifyObj.current_user_top_tracks(time_range='medium_term')['items']
    for track in results:
        if track['album']['name'] not in uniqueAlbums and len(uniqueAlbums) < 9:
            mb = MoodBlock()
            mb.album = track['album']['name']
            mb.artist = track['artists'][0]['name']
            mb.track = track['name']
            mb.audio = "https://open.spotify.com/embed/track/" + track['id']
            mb.link = track['external_urls']['spotify']
            for image in track['album']['images']:
                if image['height'] == 300:
                    mb.img = image['url']
            uniqueAlbums.append(mb.album)
            topTracks.append(mb)
        if len(uniqueAlbums) == 9:
            break
    return render(request, 'moodboard/index.html', {'moodboard': 'mood board', 'topTracks': topTracks})