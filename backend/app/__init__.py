from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # 初始化扩展
    CORS(app)
    db.init_app(app)
    
    # 注册蓝图
    from app.routes import main
    app.register_blueprint(main)
    
    return app 