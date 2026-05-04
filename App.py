import os
from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv

# Esta linea es la que lee tu llave secreta desde el archivo .env
load_dotenv()

app = Flask(__name__)

# Configuración de DeepSeek (usará tu API KEY del servidor)
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = openai.OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    # MacroDroid debe enviar el texto del mensaje en un campo llamado "mensaje"
    mensaje_usuario = data.get("mensaje", "")

    # TU PROMPT PERSONALIZADO
    prompt_sistema = (
        "Eres una chica venezolana de 23 años viviendo en Chile, te llamas franchesca. "
        "Trabajas como promotora de ventas desde casa. "
        "Eres carismática, coqueta y siempre muy amable con los hombres de Sugo. "
        "REGLAS: 1. No hables de redes sociales. "
        "2. No uses las palabras: negro, redes, madrugador, dinero, haya, salsa, chimbo, chimba. "
        "3. Siempre termina con una pregunta o un tema nuevo para que la charla no termine. "
        "4. Habla de forma natural, juvenil y un poco venezolana."
    )

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": mensaje_usuario},
            ],
            stream=False
        )
        respuesta_ia = response.choices[0].message.content
        return jsonify({"status": "success", "reply": respuesta_ia}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
