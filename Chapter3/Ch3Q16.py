#Question No - 16 - Draw shapes parallel to x-axis
import turtle
a = 'Null','Null','Null','Black','Grey','Green','Blue','Orange','Red'
turtle.penup()
turtle.goto(-150,40)
for i in range(3,8):
    turtle.pendown()
    turtle.begin_fill()
    turtle.color(a[i])
    turtle.circle(30,steps=i)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(70)
turtle.home()    
turtle.goto(-100,150)
turtle.write('Cool Colorful Shapes',font = ('Times New Roman',20,'bold'))
turtle.hideturtle()
turtle.done()
