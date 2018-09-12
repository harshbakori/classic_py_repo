def main():
    fh = open("test.txt")
    for line in fh:
        print(line.strip())
    try:
        fh = open("test1.txt")
    except IOError as e:
        print("error : ",e)
       # print("error in opning file")
    else:
        for line in fh:
            print(line.strip())
main()
