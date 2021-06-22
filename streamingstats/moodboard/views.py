from django.http import Http404
from django.shortcuts import render, redirect, reverse

import os

from .models import MoodBlock

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
# import spotipy.oauth2 as oauth2

clientID = os.environ['SPOTIPY_CLIENT_ID']
clientSecret = os.environ['SPOTIPY_CLIENT_SECRET']
redirectURI = os.environ['SPOTIPY_REDIRECT_URI']

# Create your views here.
def index(request):
    return render(request, 'moodboard/index.html', {'moodboard': 'mood board'})

def login(request):
    # print("login")
    # print(request)
    # clientID = os.environ['SPOTIPY_CLIENT_ID']
    # clientSecret = os.environ['SPOTIPY_CLIENT_SECRET']
    # redirectURI = os.environ['SPOTIPY_REDIRECT_URI']
    authManager = SpotifyOAuth(scope='user-top-read', client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI, show_dialog=True)
    return redirect(SpotifyOAuth.get_authorize_url(authManager))

def callback(request, code=None):
    # print("callback")
    code = request.GET.get("code")
    # clientID = os.environ['SPOTIPY_CLIENT_ID']
    # clientSecret = os.environ['SPOTIPY_CLIENT_SECRET']
    # redirectURI = os.environ['SPOTIPY_REDIRECT_URI']
    # print(code)
    if code is not None:
        accessToken = SpotifyOAuth.get_access_token(SpotifyOAuth(scope='user-top-read', client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI), code)
        accessToken = accessToken['access_token']
        request.session['access_token'] = accessToken
        return redirect(reverse('index'))
    else:
        return redirect(reverse('login'))

def summary(request, term='M', unique=1):
    accessToken = request.session['access_token']
    if (os.path.exists('.cache')):
        os.remove('.cache')
    print(accessToken)
    if accessToken is not None:
        sp = spotipy.Spotify(accessToken)
        print(sp.current_user()['display_name'])
        terms = {'S': 'short_term', 'M': 'medium_term', 'L': 'long_term'}
        uniqueAlbums = []
        topTracks = []
        try:
            timeRange = terms[term]
        except KeyError:
            raise Http404("Term does not exist")
        results = sp.current_user_top_tracks(time_range=timeRange)['items']
        for track in results:
            notInUniqueAlbums = True
            if unique:
                notInUniqueAlbums = track['album']['name'] not in uniqueAlbums
            if notInUniqueAlbums and len(uniqueAlbums) < 9:
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
        return render(request, 'moodboard/summary.html', {'moodboard': 'mood board', 'topTracks': topTracks, 'term': term, 'unique': unique})
    else:
        return redirect(reverse('login'))