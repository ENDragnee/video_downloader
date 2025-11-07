def download_videos(video_list: list) -> int:
    import yt_dlp

    ydl_opts: dict = {
        "format": "best",
        "outtmpl": "./output/videos/mage_build/%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for video in video_list:
            if video["type"] == "video":
                print(f"Downloading: {video['name']}")
                ydl.download([video["url"]])
            else:
                print(
                    f"Skipping non-video content: {video['name']}",
                    "Feature Under Development",
                )
    return 0
