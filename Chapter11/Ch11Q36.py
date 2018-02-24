import turtle
import random

turtle.color('gray')
x = -80
for y in range (-80,80+1,10):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
    
y = 80
turtle.right(90)
for x in range(-80,80+1,10):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(160)
        
N = 16
lattice = []
    
for i in range (N):
    lst = N * [False]
    lattice.append(lst)
        
i = (N+1)//2
j = (N+1)//2
lattice[i][j]=True
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.setheading(0)
turtle.pensize(3)
turtle.color('black')
while i>0 and i<N-1 and j>0 and j<N-1:
    if lattice[i][j+1] and lattice[i][j-1] and lattice[i-1][j] and lattice[i+1][j]:
        break
    r = random.random()  
        
    if r < .25 and not lattice[i][j+1]:
        lattice[i][j+1]=True
        j = j+1
        turtle.setheading(0)
        turtle.forward(10)
            
    elif r<.50 and not lattice[i-1][j]:
        lattice[i-1][j]=True
        i -=1
        turtle.setheading(270)
        turtle.forward(10)
            
    elif r<.75 and not lattice[i][j-1]:
        lattice[i][j-1]= True
        j = j-1
        turtle.setheading(180)
        turtle.forward(10)
         
    elif r<1.00 and not lattice[i+1][j]:
        lattice[i+1][j]=True
        i = i +1
        turtle.setheading(90)
        turtle.forward(10)
turtle.hideturtle()
turtle.done()        
                             
        
            