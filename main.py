import os
import sys
from modules.read_json_file import read_json_file, ObjectType
from modules.download_videos import download_videos
from modules.download_playlists import download_playlists
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    arg_1 = sys.argv[1] if len(sys.argv) > 1 else None
    arg_2 = sys.argv[2] if len(sys.argv) > 2 else None

    match (arg_1, arg_2):
        case (None, None):
            print("Please provide a flag and a category name.")
            sys.exit(1)
        case (None, _):
            print("Please provide a flag before the category name.")
            sys.exit(1)
        case ("-p" | "--playlists", _):
            try:
                if sys.argv[2] is None:
                    raise IndexError
                playlist_list = read_json_file(
                    os.getenv("DEFAULT_INPUT_PATH"), sys.argv[2], ObjectType.PLAYLIST
                )
                download_playlists(playlist_list, sys.argv[2])
            except IndexError:
                print(
                    "Please provide a category for the playlists name after the flag."
                )
                sys.exit(1)
        case ("-d" | "--videos", _):
            try:
                if sys.argv[2] is None:
                    raise IndexError
                video_list = read_json_file(
                    os.getenv("DEFAULT_INPUT_PATH"), sys.argv[2], ObjectType.VIDEO
                )
                download_videos(video_list, sys.argv[2])
            except IndexError:
                print("Please provide a category name for the videos after the flag.")
                sys.exit(1)
        case ("--help" | "-h", _):
            print("Usage: python main.py [flag] [category_name]")
            print("Flags:")
            print(
                "  -p, --playlists    Download playlists from the specified category."
            )
            print("  -d, --videos       Download videos from the specified category.")
            print("  -h, --help         Show this help message.")
            sys.exit(0)

        case _:
            print("Invalid flag provided. Use -p/--playlists or -d/--videos.")
            sys.exit(1)
