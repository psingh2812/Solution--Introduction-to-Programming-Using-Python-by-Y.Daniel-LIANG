x1,x2,y1,y2,z1,z2=eval(input('Enter three points for a triangle:'))
s1=((y2-x2)**2+(y1-x1)**2)**0.5
s2=((y2-z2)**2+(y1-z1)**2)**0.5
s3=((x2-z2)**2+(x1-z1)**2)**0.5
s=(s1+s2+s3)/2
a=(s*(s-s1)*(s-s2)*(s-s3))**0.5
print('Area',int(a*100)/100)