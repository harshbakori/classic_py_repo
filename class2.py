class superduck:
    def __init__(self,**kwargs):
        self.variables= kwargs
        print("object constructed ")
        
    def setval(self,varname,varvalue):
        self.variables[varname]=varvalue
        
    def getval(self,varname):
        return (self.variables.get(varname,None))
        
def main():
    #d1 = superduck(feet=2)
   # print(d1.getval())

    d2 = superduck(feet=3,color='white',feather='black')
    print(d2.getval('feet'))
    print(d2.getval('color'))
    print(d2.getval('feather'))

    
    d3 = superduck(feet=3,color='white',feather='black',eye='black',walk=True)
    d3.setval('color','blue')
    print(d3.getval('feet'))
    print(d2.getval('color'))
    print(d2.getval('feather'))
    print(d2.getval('eye'))
    print(d2.getval('walk'))

if __name__ == "__main__":main()
                   
    
main()
