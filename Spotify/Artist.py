class Artist:

    def __init__(self, artist_dict):
        self.id = artist_dict['id']
        self.name = artist_dict['name']
        self.type = artist_dict['type']

    def get_page(self, type='spotify'):
        if (type == 'spotify'):
            return 'http://open.spotify.com/artist/' + self.id
