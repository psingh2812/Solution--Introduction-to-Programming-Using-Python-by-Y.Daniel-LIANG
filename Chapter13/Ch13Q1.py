def main():
    while True:
        try:
            fn = input('Enter a filename:').strip()
            fl = open(fn,'r')
            break
        except IOError:
            print('File',fn,'does not exist.Try again')
        
    rt = input('Enter string to be removed:')
    
    lst = []
    
    for line in fl:
        changed = line.replace(rt,'')
        lst.append(changed)
        
    fl.close()
    
    fo = open(fn,'w')
    
    for line in lst:
        fo.write(line)
        
    fo.close()
    print('Done')
    
main()            
        
        