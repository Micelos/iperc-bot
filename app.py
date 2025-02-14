from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        # Twilio envía datos en formato x-www-form-urlencoded
        message = request.form.get("Body")  # Obtiene el mensaje de WhatsApp
        sender = request.form.get("From")  # Obtiene el número de quien envió el mensaje

        if not message or not sender:
            return jsonify({"error": "Datos incompletos"}), 400

        print(f"📩 Mensaje recibido de {sender}: {message}")

        # Respuesta a Twilio
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
