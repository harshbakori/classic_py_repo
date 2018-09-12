def main():
    
    a=10
    print(a,type(a))
    a,b,c=3,4,5
    print("%d %d %d"%(a,b,c))
    a,b = b,a
    print("%d %d "%(a,b))
    print ("array....")
    arr1 =[1,45,3,54,3] # if we use () brakets we cannot alter data with [] we caan ater data...
    print(type(arr1),arr1)
    arr1.append(8)
    arr1.insert(0,23)  #insert (pisition , thing to insert) ...
    arr1.insert(-1,99)
    print(type(arr1),arr1)
    
main()
