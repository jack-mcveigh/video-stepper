import os
import argparse

from .playlist_file_parser import PlaylistFileParser
from .video_player import VideoPlayer


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--playlist',
        action='store_true', default=False,
        dest='use_playlist',
        help='Use a playlist to play multiple videos'
    )

    parser.add_argument('file', help='The video or playlist file')

    parser.add_argument(
        '-f', '--fps',
        dest='fps',
        type=float,
        help='Change the fps of video playback'
    )
    parser.add_argument(
        '-l', '--loop',
        action='store_true', default=False,
        dest='enable_loop',
        help='Enable the video or playlist to loop indefinitely'
    )
    parser.add_argument(
        '-s', '--shuffle',
        action='store_true', default=False,
        dest='enable_shuffle',
        help='Shuffle the playlist before playing. Useful when --loop is used'
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    playlist_file = args.file
    playlist_path = os.path.abspath(os.path.dirname(playlist_file))

    if args.use_playlist:
        pfp = PlaylistFileParser(playlist_file)
        playlist = pfp.parse()
    else:
        playlist = [playlist_file]

    vp = VideoPlayer(
        playlist, playlist_path,
        fps=args.fps,
        loop=args.enable_loop,
        shuffle=args.enable_shuffle
    )
    vp.play()


if __name__ == '__main__':
    main()
