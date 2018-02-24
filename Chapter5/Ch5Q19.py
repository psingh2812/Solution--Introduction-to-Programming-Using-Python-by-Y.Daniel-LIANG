#Q.No19 Print the Pyramid
n = eval(input('Enter no between 1-15:'))
if(n<16 and n>0):
    for i in range(1,n+1):
        spaces=n-i
        j=i
        while(spaces > 0):
            print('  ',end=' ')
            spaces-=1
        while(j>0):
            print(format(j,'2'),end=' ')
            j-=1
        while(j+1<i):
            j=j+1
            print(format(j+1,'2'),end=' ')
        print() 
else:
    print('Wrong Input')       
                
        
        
        
        
        
    