def isSort(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
    return True

def main():
    s = input('Enter list:').split()
    
    n = [eval(x) for x in s]
    
    if isSort(n):
        print('The list is already sorted')
    else:
        print('The list is not sorted')
        
main()               