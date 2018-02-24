import turtle
import random
import math


def main():
    
    drwCircle(50,0,50)
    
    drwRectangle(-75,0, 100, 100)
   
    i=0
    while(i<10):
        x = random.randint(-125,-25)
        y = random.randint(-50,50)
        drwPoint(x,y)
        a = 2* math.pi *random.random()
        r = 50*random.random()
        x = r*math.cos(a) + 49
        y = r*math.sin(a) 
        drwPoint(x,y)
        i=i+1
    turtle.done()    
        
        



def drwRectangle (x=0,y=0,w=10,h=10):
    turtle.penup()
    turtle.goto(x+w/2,y+h/2)
    turtle.pendown()
    i=0
    while(i<4):
        if(i % 2 ==0):
            turtle.right(90)
            turtle.forward(w)
        else:
            turtle.right(90)
            turtle.forward(h)
        i=i+1      
    
    
def drwCircle(x=0,y=0,r=10):
    turtle.penup()
    turtle.goto(x,y-r)
    turtle.pendown()
    turtle.circle(r)
    
        
              
def drwPoint(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(1)
    turtle.end_fill()
    
    
main()    
                