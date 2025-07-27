from flask import Flask, render_template, request, send_from_directory
from gtts import gTTS  # Add this import at the top
import os
import uuid

app = Flask(__name__)

# Ensure audio folder exists
AUDIO_FOLDER = os.path.join("static", "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def generate_speech(text, lang="en"):
    filename = f"{uuid.uuid4().hex}.mp3"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    tts = gTTS(text=text, lang=lang)
    tts.save(filepath)

    return filename

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", audio_file=None)

@app.route("/speak", methods=["POST"])
def speak():
    text = request.form["text"]
    voice_id = request.form["voice"]
    audio_file = generate_speech(text, voice_id)
    return render_template("index.html", audio_file=audio_file)

@app.route("/static/audio/<filename>")
def serve_audio(filename):
    return send_from_directory(AUDIO_FOLDER, filename)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
# app.py
