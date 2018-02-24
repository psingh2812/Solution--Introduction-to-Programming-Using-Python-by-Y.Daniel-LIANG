def countLetters(s):
    count=0
    for ch in s:
        if(ch.isalpha()):
            count=count+1
    return(count)

def main():
    string = input('Enter String:')
    c = countLetters(string)
    print('No of letters in string are:',c)
    
main()            