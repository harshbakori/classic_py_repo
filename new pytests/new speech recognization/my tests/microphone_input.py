# input from microphone
import time
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone() #set default microphone as audio input

#sr.Microphone.list_microphone_names()  // list the microphones you have
#mic = sr.Microphone(device_index=3)   // to set the microphonr from the list of microphone index starts from 1
print("say somithing")
with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.5) # input noice reduction
    audio = r.listen(source)
    print("recognizing...")
z = r.recognize_google(audio)
print (z)

sleep(20)

#// below code is to test the recognization objects argument ////////////////////////////////
#first you have to have gueesy_game code in the same directory
#import speech_recognition as sr
#from guessing_game import recognize_speech_from_mic
#r = sr.Recognizer()
#m = sr.Microphone()
#recognize_speech_from_mic(r, m)
#///////////////////////////////////////////////////////////////////////////////////////////

