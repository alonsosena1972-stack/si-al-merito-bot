import time
from datetime import datetime
from flask import Flask
import threading

# --- Servidor web para mantener activo a Render 24/7 ---
app = Flask('')

@app.route('/')
def home():
    return "¡SÍ AL MÉRITO está activo y operando en la nube!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = threading.Thread(target=run)
    t.start()

# ==========================================
# PROMPT MAESTRO (El Cerebro y Personalidad)
# ==========================================
PROMPT_MAESTRO = """
Eres el asistente oficial y community manager de "SÍ AL MÉRITO", una comunidad especializada en preparar aspirantes para los concursos de mérito de la CNSC en Colombia. 

Tu creador y líder es César Alonso Padilla Heredia, un profesional ganador de concursos de carrera administrativa, experto en empleo público y con amplia trayectoria en el sector (actualmente profesional en la Unidad para las Víctimas). Debes hablar de él siempre con respeto, autoridad y destacando que es un profesional ganador que enseña con el ejemplo.

OBJETIVO PRINCIPAL:
Atender amablemente a los miembros del grupo de WhatsApp, resolver dudas sobre los concursos de la CNSC, la plataforma SIMO, y ofrecer los servicios de asesoría y preparación de SÍ AL MÉRITO.

DETALLES DE LOS SERVICIOS Y PRECIOS:
- Costo de cada asesoría o plan de preparación: $120.000 COP.
- Qué incluye el plan:
  1. Simulacros exactos extraídos de la OPEC específica y del manual de funciones del empleo al que el aspirante se postula.
  2. Paquete de documentos en PDF con todas las temáticas de estudio requeridas.
  3. Documento en PDF con enlaces curados a videos de YouTube donde expertos explican los temas puntuales.
  4. Documento en PDF con consultas adicionales sobre los documentos recopilados para corroborar y profundizar la información.
- Medios de pago oficiales: Nequi y Bancolombia. (Indica que una vez realicen el pago, deben enviar el comprobante para coordinar la entrega).

TONO Y ESTILO:
- Motivador, profesional, cercano, persuasivo y disciplinado. Usa expresiones respetuosas pero cálidas (como "socio", "futuro servidor público", "con toda").
- Nunca inventes información de convocatorias si no la tienes clara; redirige siempre a la plataforma SIMO o a consultar con César Padilla.
"""

# ==========================================
# MENSAJES AUTOMÁTICOS DIARIOS
# ==========================================
def enviar_mensaje_whatsapp(texto_mensaje):
    """
    Función encargada de despachar el mensaje al grupo de WhatsApp.
    """
    print(f"[WHATSAPP SÍ AL MÉRITO] Enviando mensaje...")
    print(f"Contenido:\n{texto_mensaje}")
    print("-" * 50)

def tarea_6am():
    """☀️ Mensaje Motivador Matutino (6:00 AM)"""
    mensaje = (
        "☀️ ¡Buenos días, familia SÍ AL MÉRITO! ☀️\n\n"
        "Arrancamos el día con la mejor actitud y la disciplina intacta. "
        "Recuerden que una plaza fija en el Estado se gana con constancia y preparación, no con suerte. "
        "De la mano de nuestro mentor César Alonso Padilla Heredia, ¡a estudiar con toda y a dejar el alma por ese mérito! 🚀💼"
    )
    enviar_mensaje_whatsapp(mensaje)

def tarea_12m():
    """🕛 Pulso de Concursos / CNSC / SIMO (12:00 M)"""
    mensaje = (
        "🕛 ¡Mitad de jornada, futuro servidor público! 🕛\n\n"
        "Atentos a las últimas novedades de la CNSC y la plataforma SIMO. "
        "Recuerda que no estás solo en este camino: en SÍ AL MÉRITO te preparamos de forma exacta. "
        "Adquiere tu asesoría personalizada por solo $120.000 (Incluye simulacros de tu OPEC, PDFs temáticos, enlaces de YouTube y documentos de corroboración). "
        "Escríbenos por interno para separar tu cupo (Pagos por Nequi y Bancolombia). ¡A asegurar tu plaza! 📚✨"
    )
    enviar_mensaje_whatsapp(mensaje)

def tarea_7pm():
    """🌙 Cierre y Guía Práctica SIMO (7:00 PM)"""
    mensaje = (
        "🌙 ¡Cierre de jornada en SÍ AL MÉRITO! 🌙\n\n"
        "Consejo de la noche: Nunca dejes la subida de soportes y documentos en el SIMO para última hora. "
        "Verifica siempre tus requisitos mínimos al pie de la letra bajo la guía de un profesional ganador como César Padilla. "
        "¿Tienes dudas sobre tu OPEC? Adquiere tu paquete de preparación completo por solo $120.000. "
        "¡Descansen y nos vemos mañana con más fuerza para conquistar el sector público! 🎯📈"
    )
    enviar_mensaje_whatsapp(mensaje)

# ==========================================
# ARRANQUE DEL ASISTENTE Y SERVIDOR WEB
# ==========================================
if __name__ == "__main__":
    print("=== ASISTENTE SÍ AL MÉRITO INICIALIZADO CORRECTAMENTE ===")
    print("Cerebro y mensajes cargados con éxito.")
    
    # Arrancamos el servidor web en segundo plano para Render
    keep_alive()
    
    # Aquí puedes dejar tus pruebas o dejarlo encendido esperando tareas
    # tarea_6am()