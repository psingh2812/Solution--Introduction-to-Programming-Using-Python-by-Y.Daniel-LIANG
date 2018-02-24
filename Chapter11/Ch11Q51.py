def main():
    flst = input('Enter students names and score separated by space:').split()
    l = len(flst)
    
    slst = []
    
    for i in range (0,l,2):
        slst.append([flst[i],int(flst[i+1])])
    
    slst.sort(key = lambda pair:pair[1])
    
    for s in slst:
        print(*s)    
        
main()        
        