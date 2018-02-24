#Q.No17 Rock,paper and scissor game
import random
a=random.randint(0,2)
b=eval(input('scissor(0), rock(1), paper(2) :'))
c='scissor','rock','paper'
if(a==b):
    print('The computer is',c[a],'.','You are',c[b],'too.It is a draw.' )
elif(b==0 and a==2) or (b==1 and a==0) or (b==2 and a==1):
    print('The computer is',c[a],'.','You are',c[b],'.You won.' ) 
else:
    print('The computer is',c[a],'.','You are',c[b],'.You loose') 
          
