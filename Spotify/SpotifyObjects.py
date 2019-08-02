import datetime
from dateutil.parser import parse

class Album:

    def __init__(self, album_dict):
        self.type = album_dict['album_type']
        self.artists = [Artist(a) for a in album_dict['artists']]
        self.markets = album_dict['available_markets']
        self.id = album_dict['id']
        self.release_date = parse(album_dict['release_date'])
        self.num_tracks = album_dict['total_tracks']
        self.name = album_dict['name']

    def __repr__(self):
        return self.name + f" ({self.release_date.year})"

class Track:

    def __init__(self, track_dict):
        self.album = Album(track_dict['album'])
        self.duration = track_dict['duration_ms']
        self.is_explicit = track_dict['explicit']
        self.id = track_dict['id']
        self.is_local = track_dict['is_local']
        self.name = track_dict['name']
        self.popularity = track_dict['popularity']
        self.track_number = track_dict['track_number']
        self.artists = [Artist(a) for a in track_dict['artists']]

    def __repr__(self):
        artist_string = ""
        if len(self.artists) == 1:
            artist_string = repr(self.artists[0])
        elif len(self.artists) == 2:
            artist_string = f"{repr(self.artists[0])} and {repr(self.artists[1])}"
        else:
            temp = [a.name if i != len(self.artists) else f"and {a.name}" for i, a in enumerate(self.artists)]
            artist_string = ",".join(temp)

        return f"{self.name} by {artist_string}"

class Artist:

    def __init__(self, artist_dict):
        self.id = artist_dict['id']
        self.name = artist_dict['name']
        self.type = artist_dict['type']

    def get_page(self, type='spotify'):
        if (type == 'spotify'):
            return 'http://open.spotify.com/artist/' + self.id

    def __repr__(self):
        return self.name
