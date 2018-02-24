import math

class RegularPolygon:
    def __init__(self,n=3,side=1,x=0,y=0):
        self.__n = 3
        self.__side = 1
        self.__x = 0
        self.__y = 0
    
    def mutator (self,new_n,new_side,new_x,new_y):
        self.__n = new_n
        self.__side = new_side
        self.__x = new_x
        self.__y = new_y
        
    def n_accessor(self):
        return self.__n
    
    def x_accessor(self):
        return self.__x 
       
    def y_accessor(self):
        return self.__y
    
    def side_accessor(self):
        return self.__side
         
    def getPerimeter(self):
        return self.n_accessor() *self.side_accessor()
    
    def getArea(self):
        v1 = self.n_accessor() * math.pow(self.side_accessor(),2)
        v2 = 4*math.tan(math.pi/self.n_accessor())
        
        return v1/v2
    
def main():
    rp = RegularPolygon(RegularPolygon.n_accessor,RegularPolygon.side_accessor,RegularPolygon.x_accessor,RegularPolygon.y_accessor)
    print('RegularPolygon 1-')
    
    print('Perimeter:',rp.getPerimeter())
    print('Area:',rp.getArea())
        
    rp.mutator(6,4,RegularPolygon.x_accessor,RegularPolygon.y_accessor)
    print('RegulaPolygon 2-')
    print('Area:',rp.getArea())
    print('Perimeter:',rp.getPerimeter())
    
    rp.mutator(10,4,5.6,7.8)
    
    print('RegulaPolygon3-')
    print('Area:',rp.getArea())
    print('Perimeter:',rp.getPerimeter())
    
   
    
    
    
main()    
       
            