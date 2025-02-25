import requests
from config import SPOTIFY_API_URL, SPOTIFY_ACCESS_TOKEN  # Import from config.py

def get_recommendations(mood):
    mood_mapping = {
        "happy": "pop",
        "sad": "acoustic",
        "angry": "rock",
        "neutral": "indie",
        "surprise": "electronic",
    }

    genre = mood_mapping.get(mood, "pop")
    
    headers = {"Authorization": f"Bearer {SPOTIFY_ACCESS_TOKEN}"}
    params = {"q": genre, "type": "track", "limit": 5}

    response = requests.get(f"{SPOTIFY_API_URL}/search", headers=headers, params=params)

    if response.status_code != 200:
        return []

    tracks = response.json().get("tracks", {}).get("items", [])
    
    songs = [
        {
            "name": track["name"],
            "artist": track["artists"][0]["name"],
            "image": track["album"]["images"][0]["url"],
            "url": track["external_urls"]["spotify"]
        }
        for track in tracks
    ]

    return songs
