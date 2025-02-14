from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Recibir datos de Twilio
    incoming_msg = request.form.get("Body", "").strip()

    # Respuesta en XML (TwiML)
    response_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
    <Response>
        <Message>Recibido: {incoming_msg}</Message>
    </Response>"""

    return Response(response_xml, mimetype="text/xml")

if __name__ == "__main__":
    app.run(debug=True)
