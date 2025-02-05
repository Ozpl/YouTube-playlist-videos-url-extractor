import os
from dotenv import load_dotenv
from pytube import Playlist

'''
Simple script that given YouTube's playlist url, prints url of each video.
If show_videos_titles is set to True, it also prints sequnce number and video title.
'''

show_videos_titles: bool = True

load_dotenv()

playlist: Playlist = Playlist(os.getenv('PLAYLIST_LINK'))
video_urls: list[str] = []

for url in playlist.video_urls:
    video_urls.append(url)
    
if show_videos_titles:
    for i, video in enumerate(playlist.videos):
        title = f"{video.author} - {video.title}"
        print(f"{video_urls[i]} {i+1}. {title}")
else:
    for url in video_urls:
        print(url)