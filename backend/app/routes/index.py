from flask import Blueprint, render_template

bp = Blueprint("frontend", __name__)

@bp.route("/", methods=["GET"])
def serve_index():
    return render_template("index.html")