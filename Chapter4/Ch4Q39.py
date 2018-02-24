#Q.No39-Turtle two circle's position with each other
import turtle
x1,y1,r1 = eval(input("Enter circle 1's x-,y-coordinates, and radius:"))
x2,y2,r2 = eval(input("Enter circle 1's x-,y-coordinates, and radius:"))
turtle.penup()
turtle.goto(x1,y1-r1)
turtle.pendown()
turtle.circle(r1)
turtle.penup()
turtle.goto(x2,y2-r2)
turtle.pendown()
turtle.circle(r2)
d=((x1-x2)**2+(y1-y2)**2)**0.5
if (d <= abs(r1-r2)):
    turtle.penup()
    turtle.goto(-50,50)
    turtle.write('circle 2 is inside circle1',font=('New Times Roman',15,'bold'))
elif (d <= (r1+r2)):
    turtle.penup()
    turtle.goto(-50,50)
    turtle.write('circle 2 overlaps circle1',font=('New Times Roman',15,'bold'))
else :
    turtle.penup()
    turtle.goto(-50,50)
    turtle.write('circle 2 does not overlap circle1',font=('New Times Roman',15,'bold'))
turtle.done()      