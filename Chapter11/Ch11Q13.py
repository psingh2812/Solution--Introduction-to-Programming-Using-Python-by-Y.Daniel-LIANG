def main():
    matrix=[]
    rows = eval(input('Enter no of rows in the list:'))
    for i in range(rows):
        s = input('Enter a row:')
        items = s.split()
        lst = [eval(x) for x in items]
        matrix.append(lst)
    rI,cI =locateLargest(matrix)
    
    print('The location of the largest element is at (',str(rI),',',str(cI),')')    
    
def locateLargest(matrix):
    largest = float(0)
    rI = 0
    cI = 0

    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                rI = i
                cI = j
    return (rI,cI)

main()             