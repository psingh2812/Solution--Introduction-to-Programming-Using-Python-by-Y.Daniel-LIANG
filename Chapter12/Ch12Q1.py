
def main():
    s1,s2,s3 = eval(input('Enter three sides:'))
    
    tri = Triangle(s1,s2,s3)
        
      
     
    color = input('Enter color:')
    tri.setColor(color)
    fil = eval(input('Enter 1/0 for filled(1:true,0:false):'))
    isFilled = (fil ==1)
    tri.setFilled(isFilled)
    
    
    print('the area is',tri.getArea())
    print('The perimeter is',tri.getPerimeter())
    print('Color is',tri.getColor())
    print('Filled is',tri.isFilled())
    
     

class GeometricObject:
    def __init__(self,color='green',filled=True):   
        self.__color = color
        self.__filled = filled
        
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color = color
        
    def isFilled(self):
        return self.__filled
    
    def setFilled(self,filled):
        self.__filled = filled
        
    def __str__(self):
        return 'color:'+self.__color+'and filled:'+str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self,side1=1,side2=2,side3=3):
    
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3
        GeometricObject.__init__(self)
            
                  
    def getSide1(self):
        return self.__side1
    
    def getSide2(self):
        return self.__side2
    
    def getSide3(self):
        return self.__side3
    
    def getArea(self):
        
        s=(self.__side1 + self.__side2 + self.__side3)/2
        A =round((s*(s-self.__side1)*(s-self.__side2)*(s-self.__side3)),2)
        return A
    
    def getPerimeter(self):
        return self.__side1 + self.__side2 + self.__side3
    
    def toString(self):
        return 'Triangle:side1 ='+str(self.__side1)+'side2='+str(self.__side2)+'_side3='+str(self.__side3)
     
main()                                    