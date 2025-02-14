from flask import Flask, request

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Recibe los datos de Twilio
    print("Datos recibidos:", data)
    return {"status": "OK"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
