import requests
import os

OLLAMA_BASE_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")

def generate_with_ollama(prompt: str) -> str:
    # 1. Thay đổi URL từ /api/generate thành /api/chat
    url = f"{OLLAMA_BASE_URL}/api/chat"
    
    # 2. Thay đổi cấu trúc payload từ "prompt" thành "messages"
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            # Prompt của bạn bây giờ được đặt trong một message object
            {"role": "user", "content": prompt} 
        ],
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    
    # 3. Thay đổi cách lấy kết quả trả về
    response_json = response.json()
    return response_json["message"]["content"]