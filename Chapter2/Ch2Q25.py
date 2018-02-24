
import turtle
x1,y1=eval(input('Enter center of rectangle:'))
l,w=eval(input('Enter length and width of rectangle:'))
turtle.penup()
turtle.goto(x1,y1)
x=x1+(l/2)
y=y1+(w/2)
turtle.goto(x,y)
turtle.pendown()
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(l)
turtle.right(90)
turtle.forward(w)
turtle.right(90)
turtle.forward(l)
turtle.penup()
turtle.goto(x1,y1)
turtle.done()


