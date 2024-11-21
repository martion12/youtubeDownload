import yt_dlp
import os
from flask import current_app

class VideoDownloader:
    def __init__(self):
        self.ydl_opts = {
            'format': 'best',
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
        }
    
    def get_video_info(self, url: str):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            try:
                info = ydl.extract_info(url, download=False)
                print(f"Extracted Info: {info}")
                return {
                    'title': info['title'],
                    'duration': info['duration'],
                    'view_count': info['view_count'],
                    'like_count': info.get('like_count'),
                    'thumbnail': info['thumbnail'],
                }
            except Exception as e:
                print(f"Error in get_video_info: {e}")
                raise Exception(f"Error fetching video info: {str(e)}")
    
    def download_video(self, url: str, output_path: str = None):
        if output_path is None:
            output_path = current_app.config['DOWNLOAD_FOLDER']
            
        options = {
            **self.ydl_opts,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'download': True
        }
        
        with yt_dlp.YoutubeDL(options) as ydl:
            try:
                return ydl.download([url])
            except Exception as e:
                raise Exception(f"Error downloading video: {str(e)}") 