from schemas.object_type import ObjectType


def downloader(list: list, list_name: str, object_type: ObjectType) -> None:
    import yt_dlp

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

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for item in list:
            try:
                print(print_string)
                print(
                    f"Downloading: {item
                      ['name']}"
                )
                ydl.download([item["url"]])
            except Exception as e:
                print(f"Failed to download {item['name']}: {e}")
