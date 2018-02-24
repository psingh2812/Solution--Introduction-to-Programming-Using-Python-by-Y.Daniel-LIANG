def main():
    m1 = inputMatrix(1)
    m2 = inputMatrix(2)
    
    
    sM = addM(m1,m2)
    sym = [[" "," "],['+','='],[" "," "]]
    
    print('The matrices are added as follows:')
    
    for i in range(3):
        print(str(m1[i][0])+' '+str(m1[i][1])+' '+str(m1[i][2])+' '+str(sym[i][0])+\
              str(m2[i][0])+' '+str(m2[i][1])+' '+str(m2[i][2])+' '+str(sym[i][1])+\
              str(sM[i][0])+' '+str(sM[i][1])+' '+str(sM[i][2]))
    
    
  

def inputMatrix(n):
    rows,col=3,3
    matrix = []
    m = input('Enter 9 elements for 3*3 matrix'+str(n)+':').split()
    k = 0
    for i in range(rows):
        matrix.append([])
        for j in range (col):
            lst = [float(x) for x in m]
            matrix[i].append(lst[k])
            k = k+1
    return matrix

def addM(a,b):
   
    result=[]
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(a[i][j]+b[i][j])
        result.append(row)
        
    return result  
      
main()  
    