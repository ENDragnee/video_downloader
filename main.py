import os
from modules.read_json_file import read_json_file
from modules.download_videos import download_videos
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    video_list = read_json_file(os.getenv("DEFAULT_INPUT_PATH"))
    download_videos(video_list)
