import schedule
import time

import speech_recognition as sr
from gtts import gTTS
import os

import requests

THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)

clima = {'THUNDERSTORM':'tormenta',
'DRIZZLE':'llovizna' ,
'RAIN':'lluvia' ,
'SNOW':'nieve' ,
'ATMOSPHERE': 'atmosfera' ,
'CLEAR':'despejado' ,
'CLOUDY':'nublado',
'CLOUDS':'nublado'
}

def speak(text):

    try:
        speech = gTTS(text=text, lang='es', slow=False)
        response_file = os.path.join(os.path.dirname(__file__),'captured_voice.mp3')

        speech.save(response_file)
        # os.system('afplay /Users/mari/Documents/py2/captured_voice.mp3 -r 1.2')# MacOS player
        os.system('afplay "{}" -r 1.2'.format(response_file))
        os.remove(response_file)
    except:
        print("Speech not recognised")

def climatic():
  city = 'barranquilla'
  Api_Key = "2606f769271b8d545fe3458b2b72ed9f" # Paste Your API ID Here

  final_URL = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)

  result = requests.get(final_URL)
  data = result.json()

  clim = str(data['weather'][0]['main']).upper()
  temprature = data['main']['temp']
  sensacion = data['main']['feels_like']
  humedad = data['main']['humidity']
  cordinatelon = data['coord']['lon']
  cordinatelat = data['coord']['lat']
#   print('1')
#   speak("El clima es de " + clima[clim] + " con temperatura de {} y sensación térmica de {}".format(float(temprature)/10, float(sensacion)/10))
  return "El clima es de " + clima[clim] + " con temperatura de {} grados y sensación térmica de {} grados".format(int(float(temprature)/10), int(float(sensacion)/10))

def job():
    print("I'm working...")

def lunch_time():
  # print("Ya es mediodia. Es hora del almuerzo. ¡Buen provecho!")
  speak("Ya es mediodia. Es hora del almuerzo. ¡Buen provecho!")

def early_morn():
  speak("Buenos días, bienvenido a Audacia")



# Run job every hour at the 42nd minute
# schedule.every().hour.at(":42").do(job)

# # Run jobs every 5th hour, 20 minutes and 30 seconds in.
# # If current time is 02:00, first execution is at 06:20:30
# schedule.every(2).hours.at("20:30").do(climatic)

# # Run job every day at specific HH:MM and next HH:MM:SS
# schedule.every().day.at("12:00").do(lunch_time)

# Run job on a specific day of the week
schedule.every().minute.at(":17").do(climatic)