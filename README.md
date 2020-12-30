# Streaming Stats

A collection of Spotify statistics created using Django and Spotipy.

## Key Features
![mood board gif](https://raw.githubusercontent.com/anna-liang/streaming-stats/main/media/mood-board.gif)
- Interactive mood board of a user's top 9 tracks displayed with via album art

## Installation

1. Install Django
```bash
python -m pip install Django
```

2. Install Spotipy
```bash
pip install spotipy
```

## Usage

You will need to head over to your [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) to register a new application. Once done, you will obtain a client ID, client secret, and you will need to specify a redirect URI.

Export these values as environment variables as such:
```bash
export SPOTIPY_CLIENT_ID="<SPOTIPY_CLIENT_ID>"
export SPOTIPY_CLIENT_SECRET="<SPOTIPY_CLIENT_SECRET>"
export SPOTIPY_REDIRECT_URI="<SPOTIPY_REDIRECT_URI>"
```

To start the Mood Board application, run the following command:
```bash
python manage.py runserver
```

and head over to [http://127.0.0.1:8000/moodboard/](http://127.0.0.1:8000/moodboard/).
