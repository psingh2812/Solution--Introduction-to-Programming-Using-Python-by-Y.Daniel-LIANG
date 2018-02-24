

def main():
    n = eval(input('Enter number for which you want to know sum of digits:'))
    sumDigits(n)



def sumDigits (n):
    s = 0
    
    while(n>0):
        s = s + n%10
        n = n//10
    print('Sum of Digits is:',s)   
    
main()    
     

    