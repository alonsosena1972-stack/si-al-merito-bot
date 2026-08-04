import time
import threading
import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡El bot de SÍ AL MÉRITO está activo y funcionando!", 200

# Datos de Green API (Asegúrate de que tus credenciales estén bien aquí o en variables de entorno)
idInstance = "TU_ID_INSTANCE"
apiTokenInstance = "TU_API_TOKEN"
chatId = "12036335xxxxxx@g.us" # El ID de tu grupo de WhatsApp

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

def tarea_programada():
    # Aquí puedes poner tus horarios o dejar la prueba de inicio
    pass

def correr_bot():
    # MENSAJE DE PRUEBA INICIAL: Apenas encienda el servidor, mandará esto
    enviar_mensaje_whatsapp("¡Hola equipo! 🚀 El bot de SÍ AL MÉRITO se ha conectado exitosamente a la nube.")
    
    while True:
        # Aquí puedes dejar tu lógica de horarios con schedule
        time.sleep(60)

if __name__ == "__main__":
    # Arrancamos el hilo en segundo plano para que mande la prueba y corra el ciclo
    hilo = threading.Thread(target=correr_bot)
    hilo.daemon = True
    hilo.start()
    
    # Puerto que exige Render para el servidor web
    app.run(host="0.0.0.0", port=10000)
