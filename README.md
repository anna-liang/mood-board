# Mood Board

A collection of a user's top 9 Spotify tracks organized in a mood board.

![mood board gif](/media/mood-board.gif)

Try out the live version [here](https://mood-boards.herokuapp.com/)!

## Features
- Separate mood boards for top tracks for the last 4 weeks, 6 months, and all-time.
- Filter tracks from the same album
- Interactive mood board via album art
- A provided summary of the tracks are available for listening

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
cd streamingstats
python manage.py runserver
```

and head over to [http://127.0.0.1:8000/moodboard/](http://127.0.0.1:8000/moodboard/).
