import os
import requests
from flask import Flask, request
import openai
import whisper

app = Flask(__name__)

# Cargar modelo de Whisper
model = whisper.load_model("small")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.form
    from_number = data.get("From")
    media_url = data.get("MediaUrl0")  # URL del audio enviado

    if media_url:
        # Descargar el audio desde WhatsApp
        audio_response = requests.get(media_url)
        audio_path = "audio.ogg"

        with open(audio_path, "wb") as f:
            f.write(audio_response.content)

        # Transcribir el audio
        result = model.transcribe(audio_path)
        transcribed_text = result["text"]

        # Responder con la transcripción
        response_message = f"📜 Transcripción:\n{transcribed_text}"

    else:
        response_message = "Envía un audio para transcribirlo."

    return response_message

if __name__ == "__main__":
    app.run(debug=True)
