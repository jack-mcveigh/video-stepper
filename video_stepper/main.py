import os
import sys

from playlist_file_parser import PlaylistFileParser
from video_player import VideoPlayer


def main() -> None:
    if len(sys.argv) != 2:
        print('Usage: main.py [ PLAYLIST.json | PLAYLIST.csv ]')
        return

    playlist_file = sys.argv[0]
    playlist_path = os.path.abspath(os.path.dirname(__file__))

    pfp = PlaylistFileParser(playlist_file)
    playlist = pfp.parse()

    vp = VideoPlayer(playlist, playlist_path)
    vp.play()


if __name__ == '__main__':
    main()
