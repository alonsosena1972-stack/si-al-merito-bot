import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡El bot de SÍ AL MÉRITO está activo y funcionando!", 200

# Reemplaza con tus datos reales de Green API
idInstance = "TU_ID_INSTANCE"
apiTokenInstance = "TU_API_TOKEN"
chatId = "12036335xxxxxx@g.us"

def enviar_mensaje_whatsapp(texto):
    url = f"https://api.green-api.com/waInstance{idInstance}/sendMessage/{apiTokenInstance}"
    payload = {
        "chatId": chatId,
        "message": texto
    }
    headers = {'Content-Type': 'application/json'}
    try:
        response = requests.post(url, json=payload, headers=headers)
        print("Mensaje enviado:", response.text)
    except Exception as e:
        print("Error al enviar mensaje:", e)

def correr_bot():
    enviar_mensaje_whatsapp("¡Hola equipo! 🚀 El bot de SÍ AL MÉRITO se ha conectado exitosamente a la nube.")
    while True:
        time.sleep(60)

if __name__ == "__main__":
    hilo = threading.Thread(target=correr_bot)
    hilo.daemon = True
    hilo.start()
    
    app.run(host="0.0.0.0", port=10000)
