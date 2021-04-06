import tidalapi
import json

def get_playlist():
    session = tidalapi.Session()
    session.login("rga.rdishyan@gmail.com", "raforafo11241124")

    tracks = session.get_playlist_tracks(playlist_id="6f9bc48e-b3cf-494f-931d-0fdc15b27707")

    tracks_obj = []

    for track in tracks:
        tracks_obj.append({"name": track.name, "artist": track.artist.name})

    with open("playlist.list", 'w+') as playlist:
        playlist.write(json.dumps(tracks_obj))