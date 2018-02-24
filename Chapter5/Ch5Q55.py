#Q.No55 Chess Board
import turtle
turtle.penup()
turtle.goto(-120,120) 
turtle.pendown()
for i in range(4):
    turtle.forward(240)
    turtle.right(90)
for j in range (-120,90,60):
    for i in range (-120,120,60):
        turtle.penup()
        turtle.goto(i,j)
        turtle.pendown() 
        turtle.begin_fill()
        turtle.color('black')
        for k in range(4):
            turtle.forward(30)
            turtle.left(90)  
        turtle.end_fill()   

for j in range (-90,120,60):
    for i in range (-90,120,60):
        turtle.penup()
        turtle.goto(i,j)
        turtle.pendown() 
        turtle.begin_fill()
        turtle.color('black')
        for k in range(4):
            turtle.forward(30)
            turtle.left(90)  
        turtle.end_fill()        
         
    
turtle.done()    
   