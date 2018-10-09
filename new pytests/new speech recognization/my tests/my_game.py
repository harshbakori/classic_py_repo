#speak this
import speech_recognition as sr
import time as t
r = sr.Recognizer()
mic = sr.Microphone()
print ("this is the test for py speech")
count = 0
def rec():
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5) # input noice reduction
        audio = r.listen(source) 
    z = r.recognize_sphinx(audio)
    print (z + "\n you have tryed " + str(count) + "times")
count = 0
while True:
    count+1
    print("read the below paragraph")
    t.sleep(1)
    para = "this is is that this is the two nations hurt it"
    print (para)

    rec()
    if (rec == para):
        print("you are succesfull")
        break
    else:
        print("please try again")
    if (count == 5):
        print("you loose")
