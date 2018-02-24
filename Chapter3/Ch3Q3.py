#Question-3.3- Calculating area between four cities

Ax,Ay=33.7489954,-84.3879824
Ox,Oy=28.5383355,-81.37923649999999
Sx,Sy=32.0835407,-81.09983419999998
Cx,Cy=35.2270869,-80.84312669999997
r=6371.01

import math

ax,ay = math.radians(Ax),math.radians(Ay)
ox,oy = math.radians(Ox),math.radians(Oy)
sx,sy = math.radians(Sx),math.radians(Sy)
cx,cy = math.radians(Cx),math.radians(Cy)
d= r * math.acos (math.sin(ax) * math.sin(cx) + math.cos(ax) * math.cos(cx) * \
                  math.cos(ay-cy))
d1= r * math.acos (math.sin(cx) * math.sin(sx) + math.cos(cx) * math.cos(sx) * \
                  math.cos(cy-sy))
d2= r * math.acos (math.sin(sx) * math.sin(ox) + math.cos(sx) * math.cos(ox) * \
                  math.cos(sy-oy))
d3= r * math.acos (math.sin(ox) * math.sin(ax) + math.cos(ox) * math.cos(ax) * \
                  math.cos(oy-ay))
d4= r * math.acos (math.sin(ax) * math.sin(sx) + math.cos(ax) * math.cos(sx) * \
                  math.cos(ay-sy))

s=(d+d1+d4)/2
a1=(s*(s-d)*(s-d1)*(s-d4))**0.5

s=(d2+d3+d4)/2
a2=(s*(s-d2)*(s-d3)*(s-d4))**0.5

A = a1+a2
print( 'City       Latitude     Longitude \n'\
       'Atlanta  ',str(Ax),'  ',str(Ay),'\n'\
       'Orlando  ',str(Ox),'  ',str(Oy),'\n'\
       'Savannah ',str(Sx),'  ',str(Sy),'\n'\
       'Charlotte',str(Cx),'  ',str(Cy),'\n')
print('Area enclosed between Atlanta,Savannah,Orlando & Charlotte is :',A,\
      'KM per square')