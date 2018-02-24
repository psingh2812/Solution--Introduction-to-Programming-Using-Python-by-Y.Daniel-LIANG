
def main():
    n = eval(input('Till which number you want to know count of Prime numbers:'))
    count=0
    for i in range(2,n):
        if(isPrime(i)==True):
            count=count+1
        else:
            pass
        i+=i    
    print('Number of Prime number less than',n,'are',count)
    

def isPrime (n):
    d=n//2
    while(d>1):
        if(n % d == 0):
            return(False)
        else:
            pass
        d=d-1
    return(True) 

main()