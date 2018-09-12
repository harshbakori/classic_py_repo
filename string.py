def main():
    s1 = "this is the string \n" # \n is next line
    print(s1)
    s2 = r"this is \n\n string"  # r indicate niglatation of \n
    print(s2)
    x=13
    s3=r" this is {} string".format(x) # {} contain value from x formate 
    print(s3)
    s4="string 1" " string 2" # spase is niglated ni bitvin " "
    print(s4)
    s5 = ''' this is string
this is second string
this is the end''' # ''' is used to have multipal lines
    print(s5) print('{0:_^11}'.format('hello')) # things in {} is define
    the type of formation
    print('{0:#^13}'.format('hello')) # number is
    defining total letters
    print('{0:*^9}'.format('hello'))  #use like
    setwith
    print('{0:@^8}'.format('hello'))  # 0is defining starting
    point x=5
    print(type(x))
    x=str(x)
    print(type(x))
main()
