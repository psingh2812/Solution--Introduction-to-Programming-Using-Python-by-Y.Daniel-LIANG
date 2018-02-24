
def main():
    number = eval(input('Enter number to check Palindrome:'))
    if(isPalindrome(number)):
        print('Number is Palindrome')
    else:
        print('Number is not a Palindrome')
            

def reverse(n):
    rev = 0
    while(n>0):
        rem=n%10
        rev=rev*10+rem
        n = n//10
    return(rev)

def isPalindrome(a):
    x = reverse(a)
    if(x==a):
        return(True)
    else:
        return(False)

main()    
    
    