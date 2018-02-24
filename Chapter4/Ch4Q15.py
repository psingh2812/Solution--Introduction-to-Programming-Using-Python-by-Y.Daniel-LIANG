import random
a= random.randint(100,999)
a=str(a)
d=eval(input('Enter three digit no:'))
d=str(d)
print('The lottery number is',a)
if (a == d):
    print('Exact order ,User Wins $10000')
elif (a[0]==d[1] and a[1]==d[2] and a[2]==d[0]) or \
     (a[0]==d[2] and a[1]==d[0] and a[2]==d[1]) or \
     (a[0]==d[0] and a[1]==d[2] and a[2]==d[1]) or \
     (a[0]==d[2] and a[1]==d[1] and a[2]==d[0]) or \
     (a[0]==d[2] and a[2]==d[0] and a[2]==d[2]):
    print('All digits match,User Wins $3000')
elif (a[0]==d[0] or a[0]==d[1] or a[0]==d[2]) or \
     (a[1]==d[0] or a[1]==d[1] or a[1]==d[2]) or \
     (a[2]==d[0] or a[2]==d[1] or a[2]==d[2]):
    print('One digit match,User Wins $1000')
else:
    print('No Match,No Prize') 
