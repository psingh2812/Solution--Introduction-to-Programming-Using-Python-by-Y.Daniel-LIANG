def main():
    cc = eval(input('Enter card no:'))
    if((prefixMatched(cc,4)==True or prefixMatched(cc,5)==True or prefixMatched(cc,37) or \
       prefixMatched(cc,6)==True) and (isValid(cc)==True)):
        print('The number',cc,'is valid')
    else:
        print('The number',cc,'is not valid')    
                        

# Return true if the card number is valid
def isValid(number):
    if (13<=getSize(number)<=16 ):
        sum1 = sumOfDoubleEvenPlace(number)
        sum2 = sumOfOddPlace(number)
        s = sum1 + sum2
        if (s % 10 == 0):
            return(True)
        else:
            return(False)
    else:
        return(False)    
    
            
    
# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    ln = getSize(number)
    a = str(number)
    s = 0
    while(ln>0):
        b = int(a[ln-2])
        b = getDigit(b)
        s = s+b
        ln=ln-2
    return(s)
    
    
    
# Return this number if it is a single digit, otherwise, return # the sum of the two digits
def getDigit(number):
    a = number * 2
    if(getSize(a)==1):
        return(a)
    else:
        s=a%10
        a=a//10
        s = s +a
        return(s)
        
    
    
# Return sum of odd place digits in number
def sumOfOddPlace(number):
    
    ln = getSize(number)
    a = str(number)
    s = 0
    while(ln>0):
        s = int(a[ln-1])+s
        ln=ln-2
    return(s)    
        
    
    
# Return true if the digit d is a prefix for number
def prefixMatched(number, d):
    pfix = getPrefix(number,d)
    if(pfix==d):
        return(True)
    else:
        return(False)
    
# Return the number of digits in d
def getSize(d):
    return(len(str(d)))
    
    
# Return the first k number of digits from number. If the
# number of digits in number is less than k, return number. def getPrefix(number, k):    
def getPrefix(number, k):
    ln = getSize(number)
    lk = getSize(k)
    while(ln>lk):
        number = number//10
        ln = ln-1
    return(number)  
  
main()    
    