print('Rules for Valid Password:  \n A password must have at least eight characters \n \
A password must consist of only letters and digits \n \
A password must contain at least two digits.')

p = input('Now Enter valid password:')

l = len (p) > 7
a = p.isalnum()
count=0
for i in range(10):
    count=count+ p.count(str(i))
d = count > 1        

if (l == a == d == True):
    print('Valid Password')
else:
    print('Invalid Password')    
    