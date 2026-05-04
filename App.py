from flask import Flask, request, jsonify
import requests

app = Flask(_name_)

# Aquí es donde Sugo o MacroDroid enviarán la información
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Datos recibidos:", data)
    
    # Aquí iría tu lógica con DeepSeek u OpenAI
    # respuesta = llamar_ai(data['mensaje'])
    
    return jsonify({"status": "success", "message": "Recibido"}), 200

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
