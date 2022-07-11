from operator import ge


class Song:
    pass
    count = 0
    artists = []
    genres = []
    artist_count = {}
    genre_count = {}
    def __init__(self, name, artist, genre):
        pass
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count += 1
        Song.artists.append(artist)
        Song.genres.append(genre)
        if artist in Song.artist_count.keys():
            Song.artist_count[artist] = Song.artist_count[artist] + 1
        else:
            Song.artist_count[artist] = 1
        if genre in Song.genre_count.keys():
            Song.genre_count[genre] = Song.genre_count[genre] + 1
        else:
            Song.genre_count[genre] = 1
