#Q.No 16 GCD of two number
a,b = eval(input('Enter two integers for finding GCD:'))
d = min(a,b)
while(d>1):
    
    if(a%d==0 and b%d==0):
        break
    else:
        d=d-1
print('GCD of',str(a),'and',str(b),'is :',str(d))
        