from flask import Blueprint, request, jsonify
from app.services.rag_service import generate_response

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("", methods=["POST"])
def chat():
    data = request.get_json()
    question = data.get("question", "")

    if not question:
        return jsonify({"error": "Missing 'question' in request"}), 400

    try:
        answer = generate_response(question)
        return jsonify({"answer": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
