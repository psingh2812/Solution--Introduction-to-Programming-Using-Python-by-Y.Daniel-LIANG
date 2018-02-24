def gcd(m,n):
    if m%n==0:
        return n
    else:
        return gcd(n,m%n)
        
        
def main():
    x,y = eval(input('Enter two no for finding  GCD of them:')) 
    print('GCD of',x,'and',y,'is:',gcd(x,y))       
    
main()    