import cv2
import pygame
import asyncio
import os
from multiprocessing import Process
import time
import sqlite3

import threading
import time

import pyaudio
import numpy as np


import datetime

import consult

import threading
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import test
import clima

import schedule

# Crear una instancia del chatbot
chatbot = ChatBot(
    'Example Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'a',
            'maximum_similarity_threshold': 0.90
        }
    ]
)




# Entrenamiento del chatbot
trainer = ListTrainer(chatbot)
# Promts. Antes de la coma es la input y después de la coma (los números) es la respuesta
trainer.train([ "mari Hola",
    "1"])
trainer.train([ "mary Hola",
    "1"])
trainer.train(["mari Saluda a los invitados", #sí
    "1"])

trainer.train(["mary Saluda a los invitados", #sí
    "1"])#Bienvenido a AudacIA centro de investigación
# Podrías saludar a los invitados, Mari
# Qué tal si das la bienvenida a nuestros invitados, Mari
# Mari ¿puedes decir hola a nuestros invitados
# Podrías dar un saludo a los invitados en nombre de Mari
# Mari ¿te importaría saludar a los invitados que llegaron
# Serías tan amable de saludar a los invitados Mari
# Mari podrías extenderles un cordial saludo a nuestros invitados
# Qué tal si les das la bienvenida a los invitados Mari
# Mari podrías saludar a quienes acaban de llegar
# Podrías saludar a nuestros invitados Mari

trainer.train(['mary buenos días',
               '22'])
trainer.train(['mari buenos días',
               '22'])

trainer.train(['mary buenos tardes',
               '23'])
trainer.train(['mari buenos tardes',
               '23'])

trainer.train(['mary',
               '27'])

trainer.train(['mary qué tal estás',
               '28'])
trainer.train(['mari qué tal estás',
               '28'])

trainer.train(["mari saluda a los invitados",
    "1"])#no
trainer.train(['mari saludar a los invitados', 
               '1'])#sí

trainer.train(["mary háblame de los proyectos de audacia",
               '16'])

# Mary podrías proporcionar información sobre los proyectos en los que estás trabajando
# Qué proyectos estás llevando a cabo en este momento, Mary
# Mary podrías darme una visión general de los proyectos en los que estás involucrada
# Cuáles son los proyectos más destacados en los que estás trabajando, Mary
# Mary podrías compartir algunos detalles sobre los proyectos en los que has estado trabajando recientemente
# Podrías hablar un poco sobre los proyectos actuales, Mary
# Mary qué tipo de proyectos estás gestionando en este momento
# Cuál es el enfoque principal de tus proyectos actuales, Mary
# Mary puedes darme un resumen de los proyectos en los que estás implicada
# Qué avances has logrado en tus proyectos más recientes, Mary

trainer.train(["mari háblame de los proyectos de audacia",
               '16'])

trainer.train(["mary háblanos de los proyectos de AudacIA.",
               '16'])

trainer.train(["mary Educación",
               '13'])

trainer.train(["mari Educación",
               '13'])

trainer.train(["mary Háblame de los kits robóticos",
               '4'])

trainer.train(["mari Háblame de los kits robóticos",
               '4'])

trainer.train(["mary Salud",
               '6'])

trainer.train(["mari Salud",
               '6'])

trainer.train(["mari háblame de ti",
               '15'])

trainer.train(["mary háblame de ti",
               '15'])

trainer.train(['mary quién eres',
               '15'])

trainer.train(["maria quién eres",
               '15'])

trainer.train(["mari quién eres",
               '15'])

trainer.train(["mary medio Ambiente",
               "8"])

trainer.train(["mari medio Ambiente",
               "8"])

trainer.train(["mary medioAmbiente",
               "8"])

trainer.train(["mari medioAmbiente",
               "8"])

trainer.train(['mary ambiente',
               '8'])

trainer.train(["mary háblame del dispositivo médico de los ojos",
               '9'])

trainer.train(["mari háblame del dispositivo médico de los ojos",
               '9'])

trainer.train(["mary háblame de Biotecnia",
               '12'])

trainer.train(["mari háblame de Biotecnia",
               '12'])


trainer.train(["mary háblame de la IA de detección de virus en plantas",
               '7'])

trainer.train(["mari háblame de la IA de detección de virus en plantas",
               '7'])

trainer.train(["maria háblame de la IA de detección de virus en plantas",
               '7'])

trainer.train(["mary Háblame del proyecto de detección de petróleo.",
               '10'])

trainer.train(["mari Háblame del proyecto de detección de petróleo.",
               '10'])

trainer.train(["mari Háblame del proyecto de detección de petróleo.",
               '10'])

trainer.train(["mary qué es audacia ",
               '11'])

trainer.train(["mari qué es audacia ",
               '11'])

trainer.train(["mary Cuáles son los logros de AudacIA ",
               '5'])

trainer.train(["mari Cuáles son los logros de AudacIA ",
               '5'])

trainer.train(["mary hablame de camil",
    "18"])#no

trainer.train(["mary hablame de camil",
    "18"])#no

trainer.train(["mari hablame de camille",
    "18"])#no

#IA obtenida a partir de datos simulados para atacar el virus SARS-CoV-2 (Covid 19) Demora en obtener resultados por la alta demanda de pruebas PCR en la ciudad de Barranquilla. Esta alta demanda promovía la obtención de resultados erróneos dando como negativos casos posiblemente positivos. Se generaron y probaron modelos de aprendizaje automático (ML)utilizando pequeñas cantidades de datos de cada clase. Se utilizó el mejor modelo para clasificar los big data obtenidos por el Laboratorio de Virología de la Universidad Simón Bolívar a partir de curvas de RT-PCR en tiempo real para el SARS-CoV-2, y el modelo fue reentrenado e implementado en un software que correlacionó los datos del paciente con la prueba y diagnósticos de IA. La IA se diseñó para facilitar la verificación mediante la detección de perfiles atípicos en las curvas de PCR causados por contaminación o artefactos. Se mejoró la atención de los laboratorios y la veracidad de los resultados de las muestras PCR en la ciudad de Barranquilla y Departamento del Atlántico El problema radica cuando son muchas muestras que hay que revisar por parte de los directores de laboratorios, cuando CAMILLE detecta una anomalía marca la intercepción del canal y el paciente específico, donde se debe revisar para tomar la decisión."])
trainer.train(['mary háblame de kamil',
                '18']) #sì , bajar la velocidad

trainer.train(['mari háblame de kamil',
                '18'])

trainer.train(['mary hablame de Camilo',
              '18' ])#no

trainer.train(['mari hablame de Camilo',
              '18' ])

trainer.train(['mary dime qué es Camil',
               '18'])

trainer.train(['mari dime qué es Camil',
               '18'])

trainer.train(['mary qué es Camil',
               '18'])#sí

trainer.train(['mari qué es Camil',
               '18'])

trainer.train(["mary hablame de SkinnIA",
    "20"])

trainer.train(["mari hablame de SkinnIA",
    "20"])

trainer.train(["mary hablame de Skinny",
    "20"])

trainer.train(["mari hablame de Skinny",
    "20"])

trainer.train(["mary háblame de esquinia",
                '20'])#sí

trainer.train(["mari háblame de esquinia",
                '20'])

trainer.train(['mary Hálame esquinia',
               '20'])

trainer.train(['mari Hálame esquinia',
               '20'])

trainer.train(['mary dime que es esquinia',
                '20'])#non

trainer.train(['mari dime que es esquinia',
                '20'])

trainer.train(['mary Qué es esquinia',
                '20'])#no

trainer.train(['mari Qué es esquinia',
                '20'])

trainer.train(['mary y eso es lo que hay', 
               '20'])

trainer.train(['maria y eso es lo qu hay', 
               '20'])

trainer.train(['mari háblame de ti', 
               '15'])

trainer.train(["mary cuéntame sobre vart",
    "3"])#sí

trainer.train(["mari cuéntame sobre Vart",
    "3"])

trainer.train(["mary cuéntame sobre bart",
    "3"])

trainer.train(["mari cuéntame sobre bart",
    "3"])

trainer.train(['mary dime que es bart',
               '3'])

trainer.train(['mari dime que es bart',
               '3'])

trainer.train(['mary dime que es bart',
               '3'])

trainer.train(['mari dime que es bart',
               '3'])

trainer.train(['mary qué es bart',
                '3'])#sí

trainer.train(['mari qué es bart',
                '3'])

trainer.train(['mary qué es var', 
               '3'])

trainer.train(['mari qué es var', 
               '3'])

trainer.train(['mary háblame sobre rov', 
               '29'])
trainer.train(['mary háblame sobre rob', 
               '29'])

trainer.train(['mari háblame sobre rov', 
               '29'])
trainer.train(['mari háblame sobre rob', 
               '29'])
trainer.train(['mary qué puedes decirme sobre Biotecnia',
              '12' ])

trainer.train(['mari qué puedes decirme sobre Biotecnia',
              '12' ])

# trainer.train(["Qué es Patria",
#     "20"])

trainer.train(['mary dime que es patri',
                '19'])#sí

trainer.train(['mari dime que es patri',
                '19'])

trainer.train(['mary dime que es patricia',
                '19'])

trainer.train(['mari dime que es patricia',
                '19'])

trainer.train(['Mary qué es patri',
           '19'])#sí

trainer.train(['Mari qué es patri',
           '19'])

# trainer.train(['dime qué es patri',
#                '5'])#sí

trainer.train(["mari hablame de patri", 
                "19"]) #Patrii es una IA que detecta glaucoma en segundos al analizar campos visuales. Su software autónomo es un valioso recurso para oftalmólogos, identificando anomalías y glaucoma en 20 segundos, además de ser uno de los primero software patentados en Colombia

trainer.train(["mary hablame de mario",
    "2"])#non
trainer.train(["mari hálame mario",
               "2"])#no
trainer.train(["mary háblame de mario",
    "2"])
trainer.train(['mary háblame de mario',
    '2'])#no

trainer.train(['mari háblame de mario',
    '2'])

#Bot que ayuda al entrenamiento de estudiantes de medicina en el uso de la semiología de las enfermedades El software con inteligencia artificial para fortalecer la precisión de dictámenes médicos por medio de la simulación de pacientes virtuales. Mario toma como base la simulación de pacientes virtuales que permita fortalecer conocimientos y habilidades de las personas del sector de la salud, siendo destinado principalmente a los estudiantes de dicho sector para complementar su proceso de aprendizaje. El adecuado reconocimientos de síntomas físicos es crucial en este campo profesional, por ejemplo, un pediatra se debe ser muy cuidadoso con respecto a lo que el niño trata de expresar las molestias que siente. Actualmente el uso e implementación de pacientes virtuales supone un gran avance tecnológico para la exploración de distintas ramas de la medicina. Esto impacta significativamente en las habilidades a desarrollar por el personal de la salud, como lo es la toma de diagnóstico médico, repercutiendo finalmente en la creación de la historia clínica del mismo
trainer.train(['mary dime que es mario', 
               '2'])#sí
trainer.train(["mari que es mario", 
               '2'])#sí
trainer.train(["mari cómo estás",
    "21"])
trainer.train(["mary cómo estás",
    "21"])

trainer.train(['mary cuéntame un chiste',
               '24'])

trainer.train(['mari cuéntame un chiste',
               '24'])

trainer.train(['mari tienes otro chiste',
               '25'])

trainer.train(['mary tienes otro chiste',
               '25'])

trainer.train(['Mary dime algo gracioso',
               '26'])

trainer.train(['Mari dime algo gracioso',
               '26'])

global name
name = "mari"
palabra_clave = "mary"
attemts = 0

def imprimir_saludo():
    hora_actual = datetime.datetime.now().strftime("%I:%M %p")  # Obtiene la hora actual en formato de 12 horas
    horas_saludo = ["06:27 PM", "07:20 PM", "12:00 PM"]  # Horas definidas para imprimir el saludo
    dia = ["08:00 AM", "07:40 AM", "09:00 AM"]
    pausaActiva = ["10:00 AM", "04:00 PM", "08:10 PM"]
    tarde = ["12:01"]
    comida = ["12:00 PM"]
    HNow = datetime.datetime.now().strftime("%M")
    hora_clima=["00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55"]
    MNow = datetime.datetime.now().strftime("%S")
    minuto_clima=["00", "25", "50"]
    almuerzo = 'Hola compañeros! Es hora de un merecido descanso. El reloj marca la hora del almuerzo. Les invito a recargar energías. ¡Buen provecho a todos!'
    H = datetime.datetime.now().strftime("%H")    
    rise = ["10:00 AM"]
    rage = ["02:00 PM"]
    



    # Si los minutos son 0 o 30, imprime "¡Hola!"
    if HNow in hora_clima and MNow in minuto_clima:

        print(clima.climatic())
        clima.speak(clima.climatic())
        # print("¡Hola!")

    if hora_actual in horas_saludo and MNow in minuto_clima:
        test.invitados()
        print("¡Hola!")
    if hora_actual in dia and MNow in minuto_clima: #buen día
        test.buendia()
    if hora_actual in pausaActiva and MNow in minuto_clima:# Pausa activa
        clima.speak("HORA DE PAUSA ACTIVA, A MOVERSE")
    if hora_actual in comida and MNow in minuto_clima: # Hora de almorzar
        clima.speak(almuerzo)
    if hora_actual in tarde and MHow in minnuto_clima:
        test.tarde()#buena tarde    
    if hora_actual in rise and MHow in minnuto_clima: #10:00 AM
        clima.speak("Son las 10 de la mañana")
    if hora_actual in rage and MHow in minnuto_clima: #2:00 pm
        clima.speak("Es hora de regresar a las actividades diarias")
    
    
    
    
    
def beamforming(stream, mic_positions):
    CHUNK = 1024
    channels = len(mic_positions)

    while True:
        data = stream.read(CHUNK)
        frames = [np.frombuffer(data, dtype=np.int16, offset=2*i, step=2*channels) for i in range(channels)]
        aligned_frames = [np.roll(frames[i], -i) for i in range(channels)]
        summed_frames = np.sum(aligned_frames, axis=0)
        output = np.array(summed_frames, dtype=np.int16).tobytes()
        yield output
        


def respond(query):
    response = str(chatbot.get_response(query))
    speak(response)


def listen():
    recognizer = sr.Recognizer()
    status = False # valor incial
   
   
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        rec = ""
    try:
        
        query = recognizer.recognize_google(audio, language='es-ES').lower()
        if palabra_clave in rec or name in rec:
        #if rec.startswith(palabra_clave) or rec.startswith(name):
            rec = rec.replace(f"{palabra_clave}", "").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
            status = True
        else:
            test.disculpa()
        print("Reconociendo...")
        print("Usuario:", query)
        
        # Verificar si la palabra clave está al principio de la oración
        if query.startswith(palabra_clave) or query.startswith(name):
        # if palabra_clave in rec or name in rec:
            respond(query)
        else:
            print("nno")
            # Aquí puedes manejar el caso en el que la palabra clave no está al principio
            
    except Exception as e:
        print("No pude entender lo que dijiste:", e)
    return {'text':rec, 'status':status}

def speak(query):
    print(query)
      
    if query == '1':
        test.invitados()
        
    elif query == '2':
        test.mario()
        
    elif query == "3":
        test.vart()
        
    elif query == '4':
        test.kits()
        
    elif query == '5':
        test.logros()
        
    elif query == '6':
        test.salud()
        
    elif query == '7':
        test.plantas()
        
    elif query == '8':
        test.ambiente()
        
    elif query == '9':
        test.ojos()
        
    elif query == '10':
        test.petroleo()
        
    elif query == '11':
        test.audacia()
        
    elif query == '12':
        test.biotecnia()
        
    elif query == '13':
        test.educacion()
        
    elif query == '404':
        test.disculpa
        
    elif query == '15':
        test.mari()
        
    elif query == '16':
        test.proyecto()
        
    elif query == '17':
        test.categoria()
        
    elif query == '18':
        test.camille()
        
    elif query == '19':
        test.patrii()
        
    elif query == '20':
        test.skinia()
        
    elif query == '21':
        test.comoEstas()
    
    elif query == '22':
        test.buendia()
        
    elif query == '23':
        test.tarde()
        
    elif query == '24':
        test.chiste1()
        
    elif query == '25':
        test.chiste2()
        
    elif query == '26':
        test.chiste3()
        
    elif query == '27':
        test.mary()
    
    elif query == '28':
        test.estas()
        
    elif query == '29':
        test.rov()
    else:
        test.nothing()

    
       
    #consult.eliminar_registros_tabla_statement()
    
base_dir = os.path.dirname(__file__)
saludo_m = '¡Hola! Buenos dias equipo de AudacIA, espero que tengan un dia productivo y tengan un buen avance en sus proyectos'
almuerzo = 'Hola compañeros! Es hora de un merecido descanso. El reloj marca la hora del almuerzo. Les invito a recargar energías. ¡Buen provecho a todos!'


def main():
    
    while True:
        
        test.inicio()

        imprimir_saludo()

        rec_json = listen()

        # time_runs = threading.Event()
        # time_runns.set()
        # t = threading.Thread(target=timer, args=(timer_runs,))
        # t.start()

        # time.sleep(10)
        # time_runs.clear()

        rec = rec_json['text']
        status = rec_json['status']

        if status:
            # Verificar si la palabra clave está al principio de la oración
            if rec.startswith(palabra_clave):
                respond(rec)
            else:
                print("La palabra clave no está al principio de la oración.")

if __name__ == "__main__":
    main()
