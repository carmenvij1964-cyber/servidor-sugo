from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Ruta para recibir los mensajes de Sugo/MacroDroid
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Mensaje recibido de Sugo:", data)
    
    # Aquí es donde el bot decide qué responder
    return jsonify({
        "status": "success", 
        "reply": "¡Hola! Estoy procesando tu mensaje con IA"
    }), 200

if __name__ == '__main__':
    # Usamos el puerto 5000 que es el estándar
    app.run(host='0.0.0.0', port=5000)
