import speech_recognition as sr
sr.__version__
r = sr.Recognizer()  #setting up recognizer

harvard = sr.AudioFile('harvard.wav') #selkecting the audio file

with harvard as source:
    audio = r.record(source)    #record audio for translation from source
type(audio)
z = r.recognize_google(audio)# translation request
print (z) # pritn the translated output on the screen

with harvard as source: 
     audio = r.record(source, duration=4)  #taking only first 4 seconds of source file
     #audio = r.record(source, offset=4, duration=3)   ## this offset is starting point and duration is time from starting point

z = r.recognize_google(audio) # translate
print (z) # pritn the translated output on the screen