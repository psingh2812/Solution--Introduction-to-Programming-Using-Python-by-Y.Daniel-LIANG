#Q.No3 - Solving linear equation
a,b,c,d,e,f = eval(input('Enter values a,b,c,d,e,f for equations \n'\
                         'ax + by = e \n'\
                         'cx + dy = f \n'))
if ( a * d - b * c == 0):
    print('The equation has no solution')
else :
    x = (e*d - b*f)/(a*d - b*c)
    y = (a*f - e*c)/(a*d - b*c)
    print('x is {} and y is {}'.format(format(x,'.1f'),format(y,'.1f')))    