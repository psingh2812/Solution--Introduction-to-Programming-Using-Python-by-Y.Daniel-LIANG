import urllib.request
def main():
    fn = urllib.request.urlopen('http://cs.armstrong.edu/liang/data/Lincoln.txt')
    
    s = fn.read()
    
    fn.close()
    
    print('Total no of words in speech are:',str(len(s.split())))
    
main()    