class Point:
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
        
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    
    def isNearBy(self,p):
        return self.dist(p)<5
    
    def dist(self,p):
        return((self.__x - p.__x) * (self.__x - p.__x) + (self.__y - p.__y) * (self.__y - p.__y))**0.5    
    
    def __str__(self):
        return '('+str(self._x)+','+str(self.__y)+')'
    
def main():
    x1,y1,x2,y2 = eval(input('Enter two points x1,y1,x2,y2:'))
    
    p1 = Point(x1,y1)
    p2 = Point(x2,y2)
    
    print('Distance between two point is :',p1.dist(p2))
    
    if p1.isNearBy(p2) :
        
        print('The two points are near to each other')   
        
    else:
        print('The two points are not near to each other')
        
main()
            