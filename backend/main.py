from flask import Flask
from app.controllers.chat_controller import chat_bp
from dotenv import load_dotenv
from pathlib import Path
import os

# Load .env từ thư mục gốc
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat_bp, url_prefix="/chat")
    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, port=port)