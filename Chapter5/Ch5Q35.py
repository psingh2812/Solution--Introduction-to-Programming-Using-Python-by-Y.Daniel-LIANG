#Q.No35 Finding perfect number
n = eval(input('Enter no till you want to find perfect number:'))
for i in range(1,n):
    d=i//2
    s=1
    while (d>1):
        if(i%d == 0):
            s = s+d
        d-=1
    if(i==s):
        print('Perfect Number',i)
    else:
        pass              