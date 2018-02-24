class Rational:
    
    def __init__(self, numerator = 1, denominator=0):
        if denominator == 0:
            raise RuntimeError('Denominator cannot be zero')
        divisor = gcd(numerator, denominator)
      
        self.__numerator = (1 if denominator > 0 else -1) * int(numerator/divisor)
   
        self.__denominator = int (abs(denominator))/divisor
        
 
    def __add__(self, secondRational):
        n = self.__numerator * secondRational[1] + self.__denominator * secondRational[0]
        d = self.__denominator * secondRational[1]
        return Rational(n,d)
         
    def __sub__(self, secondRational):
        n= self.__numerator * secondRational[1] - self.__denominator * secondRational[0]
        d= self.__denominator * secondRational[1]
        return Rational(n, d)
    
    def __mul__(self, secondRational):
        n = self.__numerator * secondRational[0]
        d = self.__denominator * secondRational[0]
        return Rational(n, d)

    def __truediv__(self, secondRational):
        n = self.__numerator * secondRational[1]
        d = self.__denominator * secondRational[0] 
        return Rational(n, d)
    
    def __float__(self):
        return self.__numerator/self.__denominator
    
    def __int__(self):
        return int(self.__float__())


    def __str__(self):
        if self.__denominator == 1: 
            return str(self.__numerator)
        else:
            return str(self.__numerator) +"/"+str(self.__denominator)
        
    def __lt__(self, secondRational):
        return self.__cmp__(secondRational) < 0
    
    def __le__(self,secondRational):
        return self.__cmp__(secondRational) <= 0
    
    def __gt__(self, secondRational):
        return self.__cmp__(secondRational) > 0
     
    def __ge__(self, secondRational):
        return self.__cmp__(secondRational) >=0
    
    def __cmp__(self, secondRational):
        temp = self.__sub__(secondRational) 
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0

    def __getitem__(self, index):
        if index == 0:
            return self.__numerator 
        else:
            return self.__denominator


def gcd(n, d):
   
    n1 = abs(n)
    n2 = abs(d)
    gcd = 1
    k=1
    while k<=n1 and k<=n2:
        if n1 % k == 0 and n2 % k == 0: 
            gcd = k
        k += 1
            
    return gcd

def main():
    
    r1 = Rational(4,0)

    r2 = Rational(2,3)


    print(r1,'+',r2,'=',r1+r2)
    print(r1,'-',r2,'=',r1-r2)
    print(r1,'*',r2,'=',r1*r2)
    print(r1,'/',r2,'=',r1/r2)

    print(r1,'>',r2,'is',r1>r2)
    print(r1,'>=',r2,'is',r1>=r2)
    print(r1,'<',r2,'is',r1<r2)
    print(r1,'<=',r2,'is',r1<=r2)
    print(r1,'==',r2,'is',r1==r2)
    print(r1,'!=',r2,'is',r1!=r2)

    print('int(r2) is',int(r2))
    print('float(r2) is',float(r2))
    print('r[20] is',r2[20])
    print('r2[1] is',r2[1])
    
main()    