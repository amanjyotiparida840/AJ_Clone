import pyttsx3
import datetime
import speech_recognition as sr
from speech_recognition import Microphone
import wikipedia
import webbrowser
import os
from tkinter import *


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
set_voice=engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
      print("Listening....")
      r.pause_threshold =1
      r.energy_threshold=70
      audio=r.listen(source)
     # with sr.Microphone() as source: r.adjust_for_ambient_noise(source)
     # print("Set minimum energy threshold to {}".format(r.energy_threshold))
      print(r.energy_threshold)
    try:
        print("recognizing....")
        query=r.recognize_google(audio, language='eng-in')
        print(f"user said : {query}\n")

    except Exception as e:
      #  print(e)
        print("say that again please....")
        return "None"

    return query
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning aman sir ")
    elif hour>12 and hour<18:
        speak("good afternoon aman sir")
    else:
        speak("good evening aman sir")

    speak("i am jarvis sir ,how may i help you")


def QUERY():
    while True:

      query=takecommand().lower()
      if 'wikipedia' in query:

          speak('searching wikipedia...')
          query=query.replace("wikipedia","")
          results=wikipedia.summary(query, sentences=2)
          speak("according to wikipedia")
          speak(results)
          print(results)

      elif 'open youtube' in query:
          speak('sure sir just wait')
          webbrowser.open("youtube.com")

      elif 'open any porn site' in query:
          speak('sorry sir porn web site banned in india')

      elif 'open cmd' in query:
          cmd_path='%windir%\system32\cmd.exe'
          os.startfile(cmd_path)

      elif 'open command prompt' in query:
          speak("ok sir just wait")
          cmd_path = 'C:\\Windows\\system32\\cmd.exe'
          os.startfile(cmd_path)


      elif 'open facebook' in query:
          speak('sure')
          webbrowser.open("facebook.com")

      elif 'open instagram' in query:
          speak('just wait')
          webbrowser.open("instagram.com")

      elif 'open stack overflow' in query:
          speak('sure')
          webbrowser.open("stackoverflow.com")

      elif 'open github' in query:
          speak("just wait aman sir")
          webbrowser.open("github.com")

      elif 'open git' in query:
          speak("just wait aman sir")
          webbrowser.open("github.com")

      elif 'open amazon' in query:
          speak("just wait  sir")
          webbrowser.open("amazon.in")

      elif 'open flipkart' in query:
          speak('sure')
          webbrowser.open("flipkart.com")


      elif 'open google' in query:
          speak("just wait aman sir")
          webbrowser.open("google.com")

      elif 'open bput result' in query:
          webbrowser.open("bputexam.in/studentsection/resultpublished/studentresult.aspx")

      elif 'shut your mouth' in query:
          speak('ok Aman sir')
          exit()

      elif 'exit' in query:
          speak('ok Aman sir')
          exit()

      elif 'who are you' in query:
          speak('you have to ask this to aman sir instead of me')



      elif 'time now' in query:
          strtime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir now the time is {strtime}")

      elif 'play music' in query:
          music_dir='C:\\10ord\\audio'
          songs=os.listdir(music_dir)
          os.startfile(os.path.join(music_dir,songs[6]))

      elif 'hi' in query:
          speak("hello sir")

      elif 'how are you' in query:
          speak("i'm fine")
          speak("how about you")

      elif 'how about you' in query:
            speak("i'm fine")
            speak("how about you")

      elif 'ok' in query:
          speak("yes sir")

      elif 'hey whatsup babe' in query:
          speak("fine sir and you")

      elif 'open xmpp' in query:
          speak('sure sir')
          path='C:\\xampp\\xampp-control.exe'
          os.startfile(path)

      elif 'send email' in query:
            pass

def close():
    exit()


if __name__ == '__main__':

 QUERY()
 query1 = takecommand().lower()
 # if '10% luck 20% skill 15% concentrated power of will 5% pleasure 50% pain' in query1:
 #     wishme()
 #     speak("welcome aman sir")
 #     speak("log in sucessfull")
 #
 #     root = Tk()
 #     root.geometry('200x100')
 #     btn = Button(text='Start', command=QUERY, bg='red', fg='black').pack(fill=X)
 #     btn1 = Button(text='Stop', command=close, bg='red', fg='black').pack(fill=X)
 #     root.mainloop()
 #
 #
 # else:
 #
 #    speak("sorry your voice password not match in query")
 #
