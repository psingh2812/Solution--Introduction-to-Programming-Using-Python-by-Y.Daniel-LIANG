import os.path
import sys
def main():
    keywords = {"and", "as", "assert", "break", "class","continue", \
                "def", "del", "elif", "else","except", "False", "finally", \
                "for", "from","global", "if", "import", "in", "is", "lambda",\
                "None", "nonlocal", "not", "or", "pass", "raise","return", "True", \
                "try", "while", "with", "yield"}
    fln = input('Enter Python source code file path:').strip()
    if not os.path.isfile(fln):
        print('File does not exist')
        sys.exit()
    
    infile = open(fln,'r')
    text = infile.read().split()
    
    count = 0
    for word in text:
        if word in keywords:
            count = count +1
    
    print('The no. of keywords in',fln,'is',count)
    
    
main()            
        