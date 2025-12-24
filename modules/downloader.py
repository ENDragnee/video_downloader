from schemas.object_type import ObjectType
import multiprocessing
from functools import partial
import yt_dlp


def download_struct(item: dict, print_string: str, ydl_opts: dict) -> None:
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(print_string)
            print(f"Downloading: {item['name']}")
            ydl.download(item["url"])
    except Exception as e:
        print(f"Failed to download {item['name']}: {e}")


def downloader(item_dict: dict, list_name: str, object_type: ObjectType) -> None:

    if object_type == ObjectType.VIDEO:

        ydl_opts: dict = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"./output/videos/{list_name}/%(title)s.%(ext)s",
        }
        print_string: str = "Downloading video list..."
    elif object_type == ObjectType.PLAYLIST:

        ydl_opts: dict = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"./output/playlist_lists/{list_name}/%(playlist_index)s_%(title)s.%(ext)s",
        }

        print_string: str = "Downloading playlist_lists list..."
    else:
        raise ValueError("Invalid object type provided.")

    with multiprocessing.Pool(4) as pool:
        func = partial(download_struct, print_string=print_string, ydl_opts=ydl_opts)
        pool.map(
            func,
            item_dict,
        )
