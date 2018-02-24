def main():
    while True:
        try:
            fn = input('Enter filename:').strip()
            fl = open(fn,'r')
            break
        except IOError:
            print('File does not exist.Try again')
            
    lst = fl.read()
    
    fl.close()
    
    scr = [eval(x) for x in lst.split()]
    
    count,sums=0,0
    
    for i in scr:
        count = count + 1
        sums = sums + i
        
    avg = sums/count
    
    print('Total no of scores:',count)
    print('Average of scores:',avg)
    
    
    
main()
    
    
        
                