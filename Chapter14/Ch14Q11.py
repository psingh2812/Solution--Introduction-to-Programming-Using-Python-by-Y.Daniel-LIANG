import os.path
import sys
def main():
    vow = {'a','e','i','o','u'}
    cons = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'}
    
    fln = input('Enter file path:').strip()
    if not os.path.isfile(fln):
        print('File does not exist')
        sys.exit()
    
    infile = open(fln,'r')
    text = infile.read().split()
    
    countv,countc = 0,0
    for word in text:
        for ch in word:
            if ch.lower() in vow:
                countv=countv+1
            elif ch.lower() in cons:
                countc=countc+1
                    
            
      
    
    print('The no. of vowels :',countv,'and no.of consonants:',countc)
    
    
main()            
        