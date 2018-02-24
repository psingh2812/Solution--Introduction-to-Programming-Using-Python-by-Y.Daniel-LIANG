def binaryToDecimal(binaryString):
    Dec = 0
    for ch in binaryString:
        if(ch == '0' or ch =='1'):
            Dec = int(ch)+Dec*2
        else:
            return('False')    
    return(Dec)

def main():
    bn = input('Enter binary string:')
    s = binaryToDecimal(bn)
    if(s=='False'):
        print('Entered string is not binary')
    else:    
        print('Decimal for',bn,'is',s)
    
main()
    
        