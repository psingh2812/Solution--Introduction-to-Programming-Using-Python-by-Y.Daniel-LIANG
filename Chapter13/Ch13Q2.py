def main():
    while True:
        try:
            fn = input('Enter filename:').strip()
            fl = open(fn,'r')
            break
        except IOError:
            print('File',fn,'does not exist.Try again')

    lst = fl.read()
    
    print(str(len(lst))+' characters')
    print(str(len(lst.split()))+' words')
    print(str(len(lst.split('\n')))+' line') 
    
    fl.close()
    
    
main()                
        