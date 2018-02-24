#Q.No17 Rock,paper and scissor game
import random
You,Com = 0,0
Result = True
while(Result):
    a=random.randint(0,2)
    b=eval(input('scissor(0), rock(1), paper(2) :'))
    c='scissor','rock','paper'
    if(a==b):
        print('The computer is',c[a],'.','You are',c[b],'too.It is a draw.' )
    elif(b==0 and a==2) or (b==1 and a==0) or (b==2 and a==1):
        print('The computer is',c[a],'.','You are',c[b],'.You won.' ) 
        You = You+1
    else:
        print('The computer is',c[a],'.','You are',c[b],'.You loose')
        Com = Com+1 
    if (Com-You==2 or You-Com==2):
        Result = False
        if(Com>You):
            print('Computer Wins.Total Score: Computer-',Com,'and You-',You)
        else:
            print('You Win.Total Score: Computer:',Com,'and You:',You)
    else:
        pass
              
