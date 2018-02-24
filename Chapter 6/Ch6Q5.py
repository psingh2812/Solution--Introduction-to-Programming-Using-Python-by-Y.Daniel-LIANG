def main():
    n1,n2,n3=eval(input('Enter three numbers to be sorted:'))
    displaySortedNumbers(n1, n2, n3)

def displaySortedNumbers(a1,a2,a3):
    a1,a2 = mins(a1,a2)
    a1,a3 = mins(a1,a3)
    a2,a3 = mins(a2,a3)
   
    print('The Sorted number are:',a1,a2,a3) 
    
    
def mins (x,y):
    if(x>y):
        return(y,x)
    else:
        return(x,y)

main()        
