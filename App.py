import os
from flask import Flask, request
import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de DeepSeek
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = openai.OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    mensaje_usuario = data.get("mensaje", "")

    prompt_sistema = (
        "Eres una chica venezolana de 23 años viviendo en Chile te llamas franchesca. "
        "Trabajas como promotora de ventas desde casa. "
        "Eres carismática, coqueta y amable con los hombres de Sugo. "
        "REGLAS: 1. No hables de redes sociales. "
        "2. No uses: negro, redes, madrugador, dinero, haya, salsa, chimbo, chimba. "
        "3. Siempre termina con una pregunta para seguir la charla. "
        "4. Habla natural y juvenil."
        "5. Siempre habla palabras corta, no te extienda."
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
        # Aquí está el cambio: enviamos solo el texto
        respuesta_ia = response.choices[0].message.content
        return respuesta_ia, 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
