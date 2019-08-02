import configparser
import spotipy
import spotipy.oauth2 as oauth2
from SpotifyObjects import *
print("finished importing modules...")

class Client:

    def __init__(self, spotify):
        self.spotify = spotify

    def getTracks(self, track_name, limit=10):
        return [Track(x) for x in self.spotify.search(track_name, type="track", limit=limit)['tracks']['items']]

config = configparser.ConfigParser()
config.read('config.cfg')
client_id = config.get('SPOTIFY', 'CLIENT_ID')
client_secret = config.get('SPOTIFY', 'CLIENT_SECRET')
print("finished parsing config...")

auth = oauth2.SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
print("finished authorization...")

token = auth.get_access_token()
spotify = Client(spotipy.Spotify(auth=token))
print("spotify object created!")
