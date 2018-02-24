def SumDigits(n):
    s=0
    while(n>0):
        s = s+ n%10
        n = n//10
    return(s)    

def main():
    no = eval(input('Enter Number to get Sum of Digits:'))
    print('Sum of Digits is :',SumDigits(no))
    
main()

    