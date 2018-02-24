def BSort(lst):
    run = True
    j = 1
    while (j < len(lst) and run):
        
        run = False
        for i in range (len(lst)-j):
            if(lst[i]>lst[i+1]):
                lst[i],lst[i+1] = lst[i+1],lst[i]
                run = True
        j+=1        
                
               

def main():
    l=[]
    for i in range (10):
        n = input('Enter number:')
        l.append(int(n)) 
            
    BSort(l)
    print('Sorted list:',l)
    
    
main()    
            
                    
        