def download_videos(video_list: list, category_name: str) -> int:
    import yt_dlp

    ydl_opts: dict = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": f"./output/videos/{category_name}/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for video in video_list:
            try:
                print(f"Downloading: {video['name']}")
                ydl.download([video["url"]])
            except Exception as e:
                print(f"Failed to download {video['name']}: {e}")
    return 0
