from django.http import Http404
from django.shortcuts import render, redirect

import os

from .models import MoodBlock

import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Create your views here.
def index(request, term='M'):

    clientID = os.environ['SPOTIPY_CLIENT_ID']
    clientSecret = os.environ['SPOTIPY_CLIENT_SECRET']
    redirectURI = os.environ['SPOTIPY_REDIRECT_URI']
    spOAuth = SpotifyOAuth(client_id=clientID, client_secret=clientSecret, redirect_uri=redirectURI)
    token = spOAuth.get_access_token()
    if token:
        accessToken = token['access_token']
    else:
        url = request.url
        code = spOAuth.parse_auth_response_url(url)
        if code:
            token = spOAuth.get_access_token(code)
            accessToken = token['access_token']

    if accessToken:
        spotifyObj = spotipy.Spotify(accessToken)
        user = spotifyObj.current_user()

    terms = {'S': 'short_term', 'M': 'medium_term', 'L': 'long_term'}
    uniqueAlbums = []
    topTracks = []
    try:
        timeRange = terms[term]
    except KeyError:
        raise Http404("Term does not exist")
    results = spotifyObj.current_user_top_tracks(time_range=timeRange)['items']
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
    return render(request, 'moodboard/index.html', {'moodboard': 'mood board', 'topTracks': topTracks, 'term': term})
