from flask import Blueprint, jsonify, request
from app.services.downloader import VideoDownloader

main = Blueprint('main', __name__)
downloader = VideoDownloader()

@main.route('/')
def index():
    return jsonify({"message": "YouTube Analyzer API"})

@main.route('/api/video/info', methods=['POST'])
def get_video_info():
    data = request.get_json()
    url = data.get('url')
    print(f"Received URL: {url}")
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    try:
        video_info = downloader.get_video_info(url)
        print(f"Video Info: {video_info}")
        return jsonify(video_info)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500 