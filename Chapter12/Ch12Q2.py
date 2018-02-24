def main():
    row,col = eval(input('Enter the no of rows & columns on list:'))
    table = []
    for i in range (row):
        s = input('Enter row'+str(i)+':')
        lst = [eval(x) for x in s.split()]
        table.append(lst)
        
    loc = locateLargest(table)
    print('The location of largest element is '+str(loc.getMaxValue())+' at('+str(loc.getRow())+','+str(loc.getColumn())+')') 
    


class Location:
    def __init__(self,row,col,maxm):
        self.row = row
        self.col = col
        self.maxValue = maxm
        
        
    def getColumn(self):
        return self.col
    
    def getRow(self):
        return self.row
    
    def getMaxValue(self):
        return self.maxValue  
    
def locateLargest(a):
    maxm = a[0][0]
    row = col = 0
    for i in range (len(a)):
        for j in range (len(a[i])):
            if maxm < a[i][j]:
                maxm = a[i][j]
                row = i
                col = j
            
    return Location(row,col,maxm)

main()        