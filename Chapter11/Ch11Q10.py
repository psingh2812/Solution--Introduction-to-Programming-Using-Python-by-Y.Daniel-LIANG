import random
def main():
    matrix=[]
    rows,col = 4,4
    for i in range(rows):
        matrix.append([])
        for j in range (col):
            n = random.randint(0,1)
            matrix[i].append(n)
            
    print(matrix)  
    
    rI,cI=0,0
    Sc,Sr = [],[]
    for i in range (len(matrix)):
        Sr.append(sum(matrix[i]))   
        S = 0    
        for row in matrix:
            S = S+row[i] 
        Sc.append(S)     
    
    print('The location of the largest row Index:',end=' ')
    maxm = max(Sr)      
    for i in range (len(Sr)):
        if (Sr[i] >= maxm):
            maxm = Sr[i]
            print(i,end=' ')
    
        
    print('\nThe location of the largest row Index:',end=' ')
    maxm = max(Sc)     
    for i in range (len(Sc)):
        if (Sc[i] >= maxm):
            maxm = Sc[i]
            print(i,end=' ')


main()             