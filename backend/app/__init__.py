# backend/app/__init__.py

from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app) 

    from app.controllers.chat_controller import chat_bp
    app.register_blueprint(chat_bp, url_prefix="/chat")

    return app
