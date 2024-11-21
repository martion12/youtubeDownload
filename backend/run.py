from flask import Flask, request, jsonify
from yt_dlp import YoutubeDL
import logging

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# yt-dlp 配置
ydl_opts = {
    'quiet': True,
    'no_warnings': True,
    # 添加代理设置
    'proxy': 'http://172.20.96.1:7897',
}

@app.route('/api/video/info', methods=['POST'])
def get_video_info():
    try:
        data = request.get_json()
        url = data.get('url')
        logger.info(f"收到视频URL请求: {url}")

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            video_info = {
                'title': info.get('title'),
                'author': info.get('uploader'),
                'length': info.get('duration'),
                'thumbnail_url': info.get('thumbnail'),
                'formats': [
                    {
                        'format_id': f['format_id'],
                        'ext': f['ext'],
                        'resolution': f.get('resolution', 'N/A'),
                        'filesize': f.get('filesize', 0),
                        'url': f.get('url')
                    }
                    for f in info['formats'] if f.get('url')
                ]
            }
            
            return jsonify(video_info)

    except Exception as e:
        logger.error(f"处理请求时出错: {str(e)}")
        return jsonify({'error': str(e)}), 500

# 添加 CORS 支持
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

if __name__ == '__main__':
    app.run(debug=True)