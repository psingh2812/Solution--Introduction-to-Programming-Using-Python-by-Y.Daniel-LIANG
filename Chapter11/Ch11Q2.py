def main():
    matrix =[]
    r = 4
    for i in range(r):
        s = input('Enter row for a 4 by 4 matrix -row:'+str(i+1)+':').split()
        n = [eval(x) for x in s]
        matrix.append(n)

    print('\n\nSum of the elements in the major diagonal is',SoM(matrix))
    
def SoM(m):
    t =0
    for r in range(len(m)):
        t = t + m[r][r]
    return t        

main()        
        
        