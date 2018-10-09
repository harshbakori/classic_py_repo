#speak this
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
print ("this is the test for py speech")

with mic as source:
    r.adjust_for_ambient_noise(source,duration=0.5) # input noice reduction
    audio = r.listen(source) 
z = r.recognize_google(audio)
