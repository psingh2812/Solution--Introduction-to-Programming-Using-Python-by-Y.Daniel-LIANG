w=eval(input('Enter weight in pounds:'))
h=eval(input('Enter heights in inches:'))
w=w*0.45359237
h=h*0.0254
print(round((w/(h*h)),4))