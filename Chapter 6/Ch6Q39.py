import turtle

def drawLine(x1,y1,x2,y2,color = 'black',size=1):
    turtle.pen(pencolor=color,pensize=size)
    turtle.penup()
    turtle.goto(x1,y1)
    turtle.pendown()
    turtle.goto(x2,y2)
    
def main():
    drawLine(50,50,-150,50)
    drawLine(-150,50,11.80,-67.56)
    drawLine(-50,122.65,-111.80,-67.66)
    drawLine(-111.80,-67.66,50,50)
    drawLine(11.80,-67.56,-50,122.65)
    turtle.done()
    
main()
    
        
    