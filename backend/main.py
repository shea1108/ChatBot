# backend/main.py
from flask import Flask
from app.routes.index import bp as frontend_bp
from app.controllers.chat_controller import chat_bp
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
FRONTEND_DIR = os.path.join(BASE_DIR, "..", "frontend")

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.join(FRONTEND_DIR, "templates"),
        static_folder=os.path.join(FRONTEND_DIR, "static")
    )

    app.register_blueprint(frontend_bp)
    app.register_blueprint(chat_bp, url_prefix="/chat")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)
