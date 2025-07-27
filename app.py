from flask import Flask, render_template, request, send_from_directory
import pyttsx3
import os
import uuid

app = Flask(__name__)

# Ensure audio folder exists
AUDIO_FOLDER = os.path.join("static", "audio")
os.makedirs(AUDIO_FOLDER, exist_ok=True)

def generate_speech(text, voice_id=None):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Select voice or default
    selected_voice = next((v for v in voices if voice_id in v.id), voices[0])
    engine.setProperty('voice', selected_voice.id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', 1.0)

    # Save audio to file
    filename = f"{uuid.uuid4().hex}.wav"
    filepath = os.path.join(AUDIO_FOLDER, filename)

    engine.save_to_file(text, filepath)
    engine.runAndWait()

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
