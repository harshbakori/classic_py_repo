def main():
    fun4(s1="chirag",s2="priya",s3="kava")
    fun5(1,2,3,4,5,6,7,chirag='foo',jay='genious',animal='z00')
    print(fun6())
def fun4(**kwargs):
    print("arguments are",kwargs['s1'],kwargs['s2'],kwargs['s3'])

def fun5(a=1,b=2,c=3,*args,**kwargs):
    print(" a,b,c = ",a," ",b," ",c)
    for n in args:
        print(n,end=' ')
    for i in kwargs:
        print(i,' = ',kwargs[i])
def fun6():
    return 'hi hello'
main()
