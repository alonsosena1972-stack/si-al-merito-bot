import time
import requests
import schedule
from flask import Flask

app = Flask(__name__)

# Credenciales de Green API y Grupo SÍ AL MÉRITO
ID_INSTANCE = "710722700480"
API_TOKEN = "18b5dcaa690642efb742ed9723acd5589e30008802f04bfb93"
GROUP_ID = "120363294167447776@g.us"


def enviar_mensaje_whatsapp(mensaje):
  url = (
      f"https://7107.api.greenapi.com/waInstance{ID_INSTANCE}/sendMessage/"
      f"{API_TOKEN}"
  )
  payload = {"chatId": GROUP_ID, "message": mensaje}
  headers = {"Content-Type": "application/json"}

  try:
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
      print("¡Mensaje enviado con éxito al grupo SÍ AL MÉRITO!")
    else:
      print(f"Error al enviar: {response.text}")
  except Exception as e:
    print(f"Excepción en la conexión: {e}")


def tarea_6am():
  mensaje = (
      "☀️ *¡Buenos días, aspirantes de SÍ AL MÉRITO!* \nComenzamos el día"
      " con toda la energía. Revisemos el aplicativo SIMO y las OPEC"
      " disponibles para alcanzar nuestro objetivo."
  )
  enviar_mensaje_whatsapp(mensaje)


def tarea_12pm():
  mensaje = (
      "🕛 *¡Reporte del Mediodía - SÍ AL MÉRITO!* \nContinuamos activos"
      " revisando convocatorias y preparando nuestras hojas de vida en el"
      " SIGEP II. ¡A mantener el enfoque!"
  )
  enviar_mensaje_whatsapp(mensaje)


def tarea_7pm():
  mensaje = (
      "🌙 *¡Buenas noches, equipo SÍ AL MÉRITO!* \nCerramos la jornada de"
      " hoy. Repasemos los conceptos claves de administración pública y"
      " prepárense para descansar. ¡Mañana vamos por más!"
  )
  enviar_mensaje_whatsapp(mensaje)


# Programación de los horarios
schedule.every().day.at("06:00").do(tarea_6am)
schedule.every().day.at("12:00").do(tarea_12pm)
schedule.every().day.at("19:00").do(tarea_7pm)


@app.route("/")
def home():
  return (
      "Bot de SÍ AL MÉRITO operando al 100% con Green API y conectado al"
      " grupo oficial."
  )


def ejecutar_horarios():
  while True:
    schedule.run_pending()
    time.sleep(1)


if __name__ == "__main__":
  import threading

  t = threading.Thread(target=ejecutar_horarios)
  t.daemon = True
  t.start()
  app.run(host="0.0.0.0", port=10000)
