#Q.No21 Zeller's Congruence Theorem
y = eval(input('Enter year:(eg., 2008):'))
m = eval(input('Enter month: 1-12:'))
if(m==1):
    m=13
    y=y-1
elif(m==2):
    m=14
    y=y-1
else:
    pass
d = eval(input('Enter the day of the month:1-31:'))  
day = 'Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'
j = (y/100)//1
k = (y%100)
h = (d + ((26*(m+1))/10)//1 + k + (k/4)//1 + (j/4)//1 + 5*j ) % 7 
print('Day of the week is',day[int(h)])     
