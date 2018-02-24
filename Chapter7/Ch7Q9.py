class LinearEquation:
    def __init__(self,a,b,c,d,e,f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
        
        
    def geta(self):
        return float(self.__a)    
    
    def getb(self):
        return float(self.__b)
    
    def getc(self):
        return float(self.__c)
    
    def getd(self):
        return float(self.__d)
    
    def gete(self):
        return float(self.__e)
    
    def getf(self):
        return float(self.__f)
    
    def isSolvable(self):
        if(self.__a*self.__d - self.__b * self.__c  != 0):
            return True
        else:
            return False
        
    def getX(self):
        v = self.__e * self.__d - self.__b * self.__f
        v1 = self.__a * self.__d - self.__b * self.__c
        return v/v1
    
    def getY(self):
        v = self.__a * self.__f - self.__e * self.__c
        v1 = self.__a * self.__d - self.__b * self.__c
        return v/v1

    
def main():
    
    x1,y1,x2,y2= eval(input('Enter values of co-ordinates (x1,y1) & (x2,y2):'))
    a = y1-y2
    b = x2-x1
    e = -(x1*y2 - x2 * y1)
    
    
    x3,y3,x4,y4= eval(input('Enter values of co-ordinates (x3,y3) & (x4,y4):'))
    c = y3-y4
    d = x4-x3
    f = -(x3*y4 - x4*y1)
    
    eq = LinearEquation(a,b,c,d,e,f)
    if(eq.isSolvable()):
        print('Point of Intersection is:')
        print('X is equals to:',eq.getX())
        print('Y is equals to:',eq.getY())
    else:
        print('Linear are parallel')    

main()
