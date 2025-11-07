def download_playlists(playlist_list: list, playlist_name: str) -> int:
    import yt_dlp

    ydl_opts: dict = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": f"./output/playlist_lists/{playlist_name}/%(playlist_index)s_%(title)s.%(ext)s",
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for playlist in playlist_list:
            try:
                print(f"Downloading: {playlist['name']}")
                ydl.download([playlist["url"]])
            except Exception as e:
                print(f"Failed to download {playlist['name']}: {e}")
    return 0
