def main():
    fun0(1,2,3)
    fun1()
    fun1(1,3)
    fun1(1,3,5)
    fun2(1,2,3,4,5,6,7,8,9,10)
    
def fun0(one,two,three):
    
    print("arguments are",one," ",two," ",three)

def fun1(one=2,two=None,three=3,*args):
   # if two is None:
    #    two=54
    print("arguments are",one," ",two," ",three)
def fun2(one=2,two=None,three=3,*args):
   # if two is None:
    #    two=54
    print("arguments are",one," ",two," ",three)
    for n in args:
        print(n,end=' ')
main()
