from django.apps import AppConfig

import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-top-read"

spotifyObj = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

class MoodboardConfig(AppConfig):
    name = 'moodboard'
