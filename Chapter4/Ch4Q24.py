#Card picking simulation
import random
a = random.randint(0,51)
print('Random number is :',a)
print('The card you picked is',end=' ')
if (a%13==0):
    print('Ace',end=' ')
elif (a%13==10):
    print('Jack',end=' ')
elif (a%13==11):
    print('Queen',end=' ')
elif (a%13==12):
    print('King',end=' ')
else:
    print(a%13+1,end=' ')
print('of',end=' ')
if (a//13==0):
    print('Clubs')
elif (a//13==1):
    print('Diamonds')
elif (a//13==2):
    print('Hearts')
else:
    print('Spades')
    