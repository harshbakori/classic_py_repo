hi1 = "help"
hi=10.99
ha = [1,2,3,4,"hi",4,5,]
#print((str)hi + "the type is" + hi1 , type(hi1))
name = input ("Enter your name : ")
if len(name)<5:
    print ("invalid name")
else :
    print("Done thanks " + name.capitalize() + ".")

print(ha[2],type(ha[2]))
print(ha[4],type(ha[4]))

for item in ha:
    if type(item)==int:
        print(item + 10)
    else :
        print(item + " 10 ",type(item))

def hi(me,age):
    print("name is " + me.capitalize())
    print("age is "+ str(age))
    return 0
hi("hit",10)
file = open("bot.py","r")
content = file.read()
fil = open("the.txt","w")
fil.write(content)
print("file done")
fil.close()
file.close()
