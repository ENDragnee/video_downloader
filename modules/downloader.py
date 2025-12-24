import multiprocessing
from functools import partial
import yt_dlp
from schemas.object_type import ObjectType
import os


def download_struct(item: dict, print_string: str, ydl_opts: dict) -> None:
    try:
        # Each worker process creates its own YoutubeDL instance
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"{print_string} -> {item['name']}")
            # ydl.download expects a list of strings
            ydl.download([item["url"]])
    except Exception as e:
        print(f"Failed to download {item['name']}: {e}")


def downloader(video_list: list, list_name: str, object_type: ObjectType) -> None:
    if object_type == ObjectType.VIDEO:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"./output/videos/{list_name}/%(title)s.%(ext)s",
            "quiet": True,  # Recommended to avoid messy logs in parallel
            "no_warnings": True,
        }
        print_string = "Downloading video"
    elif object_type == ObjectType.PLAYLIST:
        ydl_opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "outtmpl": f"./output/playlist_lists/{list_name}/%(playlist_index)s_%(title)s.%(ext)s",
        }
        print_string = "Downloading playlist"
    else:
        raise ValueError("Invalid object type")

    # Use Pool and pass ydl_opts instead of the ydl instance
    with multiprocessing.Pool(int(os.getenv("DEFAULT_POOL_SIZE"))) as pool:
        func = partial(download_struct, print_string=print_string, ydl_opts=ydl_opts)
        pool.map(func, video_list)
