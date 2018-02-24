#Q.No29 Geometry:Two Circle

x1,y1,r1 = eval(input("Enter circle 1's x-,y-coordinates, and radius:"))
x2,y2,r2 = eval(input("Enter circle 2's x-,y-coordinates, and radius:"))
d=((x1-x2)**2+(y1-y2)**2)**0.5
if (d <= abs(r1-r2)):
    print('circle 2 is inside circle1')
elif (d <= (r1+r2)):
    print('circle 2 overlaps circle1')
else :
    print('circle2 does not overlap circle1')    
    
    