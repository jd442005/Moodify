from flask import Flask, render_template, request, jsonify
import os
from utils.mood_detection import detect_mood
from utils.spotify_api import get_recommendations

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "photo" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files["photo"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    mood = detect_mood(filepath)
    if not mood:
        return jsonify({"error": "Could not detect mood"}), 500

    songs = get_recommendations(mood)
    return jsonify({"mood": mood, "songs": songs})

if __name__ == "__main__":
    app.run(debug=True)
