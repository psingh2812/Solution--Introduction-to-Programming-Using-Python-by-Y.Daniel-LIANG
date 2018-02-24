#Q.No4 Addition of two no by generating random integers
import random
a,b = random.randint(0,100),random.randint(0,100)
s = eval (input('Enter addition of ' +str(a) +' and ' +str(b) +' :'))
if(s==a+b):
    print('True')
else:
    print('False')    