n = eval(input('Enter 4-digit integer:'))
r = 0
while(n > 0):
    r = r*10 + (n % 10)
    n = n // 10
    
print('The reversed number is:',r)