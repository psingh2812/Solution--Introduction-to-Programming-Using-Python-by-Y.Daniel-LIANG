a,b= eval(input('Enter subtotal and gratuity rate:'))
g= (a*b)/100
b=a+g
print('The gratuitu is',int(g*100)/100,'and total is',int(b*100)/100)