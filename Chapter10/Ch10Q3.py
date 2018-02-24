st = input('Enter integers between 1 to 100 separated by space:').split()
n = [eval(x) for x in st]
countL = 100 *[0]
for i in range(len(n)):
    countL[n[i]-1] += 1

for i in range (len(countL)):
    if countL[i]>0:
        if countL[i]==1:
            print(i+1,'occurs 1 time')
        else:
            print(i+1,'occurs',countL[i],'times')
            
                
            

