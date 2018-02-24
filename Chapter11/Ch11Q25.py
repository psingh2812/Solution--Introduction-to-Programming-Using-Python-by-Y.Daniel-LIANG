import sys
def main():
    matrix=[]
    row = 3
    col = 3
    print('Enter a 3*3 matrix row for row:')
    for i in range (row):
        string = input()
        items = string.split()
        n_lst = [eval(x) for x in items]
        matrix.append(n_lst)
    isMarkov(matrix)

def isMarkov(m):
    for i in range (0,len(m[0])):
        s = 0
        for row in m:
            if row[i]>0:
                s = s+row[i]
            else:
                print('Not Markov matrix')
                sys.exit()
    if s ==1:
        print('Markov matrix')
    else:
        print('Not Markov matrix')
        sys.exit()
        
    
    
main()                                
        