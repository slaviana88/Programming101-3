import datetime
import random
import time
from tabulate import tabulate
import json
import os
import mutagen


class Song:
    def __init__(self, title, artist, album, length):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__length = length

    def title(self):
        return self.__title

    def artist(self):
        return self.__artist

    def album(self):
        return self.__album

    def __str__(self):
        return "{} - {} from {} - {}".format(
            self.artist(), self.title(), self.album(), self.lenght())

    def __eq__(self, other):
        return self.title() == \
               other.title() and \
               self.artist() == other.artist()

    def __hash__(self):
        return hash(self.__str__())

    def get_length(self):
        return self.__length

    def prepare_json(self):
        song_dict = self.__dict__
        return {key: song_dict[key] for key in song_dict if not key.startswith("_")}

    def length(self, seconds=False, minutes=False, hours=False):
        result = self.__length.split(":")
        if seconds is True:
            if len(result) == 2:
                return int(result[0]) * 60 + int(result[1])
            elif len(result) == 3:
                return int(result[0]) * 3600 + int(result[1]) * 60 + int(result[2])
        elif minutes is True:
            if len(result) == 2:
                return int(result[0])
            elif len(result) == 3:
                return int(result[0]) * 60 + int(result[1])
        elif hours is True:
            return int(result[0])
        return self.__length


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):
        self.__name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.__Playlist = []
        self.__current_song_index = 0
        self.__shuffle_played_songs = set()

    def add_song(self, song):
        self.__Playlist.append(song)

    def remove_song(self, song):
        try:
            self.__Playlist.remove(song)
        except ValueError:
            pass

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        sumsongs = 0
        for song in self.__Playlist:
            sumsongs += song.length(minutes=True)
        return str(sumsongs)

    def artists(self):
        artistsdict = {}
        for song in self.__Playlist:
            if song.artist not in artistsdict:
                artistsdict[song.artist] = 0
        for song in self.__Playlist:
            if song.artist in artistsdict.keys():
                artistsdict[song.artist] += 1
        return artistsdict

    def __has_next_song(self):
        return self.__current_song_index < len(self.__Playlist)

    def __shuffle(self):
        song = random.choice(self.__Playlist)
        while song in self.__shuffle_played_songs:
            song = random.choice(self.__Playlist)

        self.__shuffle_played_songs.add(song)

        if len(self.__shuffle_played_songs) == len(self.__Playlist):
            self.__shuffle_played_songs = set()

        return song

    def next_song(self):
        if self.repeat == "SONG":
            return self.__Playlist[self.__current_song_index]

        if self.shuffle:
            return self.__shuffle()

        if not self.__has_next_song() and self.repeat == "NONE":
            raise Exception("End of the  playlist")

        if not self.__has_next_song() and self.repeat == "PLAYLIST":
            self.__current_song_index = 0

        song = self.__Playlist[self.__current_song_index]
        self.__current_song_index += 1

        return song

    def pprint_playlist(self):
        headers = ["Artist", "Song", "Length"]
        table = []

        for song in self.__Playlist:
            table.append([song.artist, song.title, song.get_length()])

        print(tabulate(table, headers=headers))

    def prepare_json(self):
        data = {
            "name": self.__name,
            "songs": [song.prepare_json() for song in self.__Playlist]
        }

        return data

    def save(self, indent=True):
        filename = self.__name.replace(" ", "-") + ".json"

        with open(filename, "w") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open(filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            playl = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song[
                            "title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return playl

    def test_load():
        p = Playlist.load("Manowar-songs.json")
        try:
            while True:
                song = p.next_song()
                print(str(song))
                time.sleep(1)
        except Exception as e:
            print(e)


    def test_save():
        s = Song(album="The Sons of Odin",
             title="Odin",
             artist="Manowar",
             length="3:44")
        s1 = Song(album="The Sonds of Odin",
              title="Sons of Odin",
              artist="Manowar",
              length="6:08")
        p = Playlist("Manowar songs", repeat="SONG")
        p.add_song(s)
        p.add_song(s1)
        p.add_song(Song(album="Fallen",
                    title="Bring Me To Life (radio edit)",
                    artist="Evanesence",
                    length="3:30"))

        p.pprint_playlist()

        p.save()


class MusicCrawler:
    def __init__(self, path):
        self.path = path
        self.data = []

    def get_data(self):
        for root, dirs, files in os.walk(self.dir):
            for filename in files:
                path = os.path.join(root, filename)
                if filename.endswith(".ogg") or filename.endswith(".mp3"):
                    song = mutagen.File(path, easy=True)
                    self.data.append(
                        Song(song['title'][0],
                             song['artist'][0],
                             song['album'][0],
                             song['length'][0]))

    def generate_playlist(self, playname="", shuff=False, repp=True):
        new_playlist = Playlist(name=playname, shuffle=shuff, repeat=repp)
        for song in self.data:
            new_playlist.add_song(song)
        return new_playlist
