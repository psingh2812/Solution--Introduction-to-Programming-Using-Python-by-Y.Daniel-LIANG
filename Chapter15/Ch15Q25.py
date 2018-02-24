import os
def main():
    path = input('Enter a directory or a file:')
    try:
        print('The number of files is '+str(getNumberofFiles(path)))
    except:
        print('Files or directory does not exist')
 
 
def getNumberofFiles(path):
    count = 0
    
    if not os.path.isfile(path):
       
        lst=os.listdir(path)
        
        for i in range(len(lst)):
            count += getNumberofFiles(path +'/'+ lst[i])
    
    else:
        count += 1
    return count 

main()                   