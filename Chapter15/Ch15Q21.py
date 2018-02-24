def binaryToDecimal(binaryString,low,high):
    if high<0:
        return 0
    else:
        temp = ord(binaryString[high])-ord('0')    
    
    return binaryToDecimal(binaryString,low,high-1)*2+temp

def main():
    bn = input('Enter binary string:')
    for ch in bn:
        if(ch == '0' or ch =='1'):
            Ok = True
        else:
            Ok = False
            break
    if (Ok):
        s = binaryToDecimal(bn,0,len(bn)-1)
        print('Decimal for',bn,'is',s)  
    else:
        print('Entered string is not binary')    
        
    
main()