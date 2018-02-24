def main():
    m1 = inputMatrix(1)
    m2 = inputMatrix(2)
    
    
    sM = PrdM(m1,m2)
    sym = [[" "," "],['+','='],[" "," "]]
    
    
    print('The matrices are added as follows:')
    
    for i in range(len(m1)):
        print(str(m1[i][0])+' '+str(m1[i][1])+' '+str(m1[i][2])+' '+str(sym[i][0])+\
              str(m2[i][0])+' '+str(m2[i][1])+' '+str(m2[i][2])+' '+str(sym[i][1])+\
              str(sM[i][0])+' '+str(sM[i][1])+' '+str(sM[i][2]))
    
    
  

def inputMatrix(n):
    rows,col=3,3
    matrix = []
    m = input('Enter matrix'+str(n)+':').split()
    k = 0
    for i in range(rows):
        matrix.append([])
        for j in range (col):
            lst = [float(x) for x in m]
            matrix[i].append(lst[k])
            k = k+1
    return matrix

def PrdM(a,b):
   
    result=[[0 for row in range(3)] for col in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += round(a[i][k] * b[k][j],1)
    
    return result  
      
main()  
