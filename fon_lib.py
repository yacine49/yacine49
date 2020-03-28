import speech_recognition as sr
from gtts import gTTS;from fbchat import Client;from fbchat.models import *
import os,json
import time
import playsound
from googletrans import Translator
import sys
import time;from ast import literal_eval
def Login(session=None):
  if session == None:
    email = input('please enter your email ')
    passwd = input('please enter your password ')
    client = Client(email, passwd)
    new_session = client.getSession()
    with open('session_json.txt', 'r+',encoding='utf-8-sig') as f:
      datastore = json.load(f)
      datastore[email] = "{}".format(new_session)
      f.seek(0)
      f.truncate()
      json.dump(datastore,f)
  else:
    with open('session_json.txt', 'r+',encoding='utf-8-sig') as f:
      datastore = json.load(f)
      session = datastore[session]
      session= literal_eval(session) 
      client = Client('yuryu-2016@hotmail.com', 'Yacine=2019', session_cookies=session)
  return client    

def effect(text):
  m = text
  M = m.upper()
  for i in range(0,len(m)):

    m=m.replace(m[i], M[i],1)
        
    print('%s\r'%m)
    time.sleep(0.2)
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')

def trans(text) :
  translator = Translator()
  tr = translator.translate(text,dest='ar')
  print(tr.text)
  return tr.text


def speak(text,lg='en'):
    tts = gTTS(text=text, lang=lg)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

def recognize():
      recognized = False
      r = sr.Recognizer()
      while recognized==False:
        try:
          with sr.Microphone() as source:
              print("Speak Anything :")
              audio = r.listen(source)            
          speech = r.recognize_google(audio)
            #print("You said : {}".format(speech))
          return speech
        except:
            print("Sorry could not recognize what you said")


