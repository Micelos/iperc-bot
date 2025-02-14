from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.get_json()  # Asegura que Flask reciba JSON
        print("Datos recibidos:", data)
        return jsonify({"status": "OK"}), 200  # Respuesta en formato JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # Manejo de errores

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

