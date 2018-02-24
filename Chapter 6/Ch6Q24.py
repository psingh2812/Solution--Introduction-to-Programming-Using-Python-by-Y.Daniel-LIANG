def main():
    count,n=0,2
    while(count<100):
        if(isPrime(n)==True and isPalindrome(n)==True):
            count=count+1
            print(format(n,'10d'),end=' ')
            if(count%10==0):
                print()
            else:
                pass    
            
        else:
            pass
        n=n+1
       
        
          

def reverse(n2):
    rev = 0
    while(n2>0):
        rem=n2%10
        rev=rev*10+rem
        n2 = n2//10
    return(rev)

def isPalindrome(a):
    x = reverse(a)
    if(x==a):
        return(True)
    else:
        return(False)
    
    
def isPrime (n1):
    d=n1//2
    while(d>1):
        if(n1 % d == 0):
            return(False)
        else:
            pass
        d=d-1
    return(True)
  
main()  