#Q.No 5 - Print the day
a = 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'
b = eval(input('Enter todays day :'))
c = eval(input('Enter the number of days elapsed since today :'))
f = (b+c)%7
print('Today is',a[b],'and future day is',a[f])