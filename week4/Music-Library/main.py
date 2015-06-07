from playlist import Playlist
from songg import Song, MusicCrawler
import time


def main():

    crawler = MusicCrawler("/home/rositsazz/music")
    zrock = crawler.generate_playlist(playname="Test")
    zrock.pprint_playlist()
    zrock.save()
    # p.save()


if __name__ == '__main__':
    main()
