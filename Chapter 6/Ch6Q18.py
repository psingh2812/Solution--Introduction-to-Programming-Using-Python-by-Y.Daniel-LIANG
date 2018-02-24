def main():
    n = eval(input('Enter n:'))
    printMatrix(n)
    
def printMatrix(n):
    import random
    for i in range(0,n):
        for j in range(0,n):
            print(random.randint(0,1),end=' ')
        print()    
        
main()                