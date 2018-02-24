#Q.No30 Print 1st day of Year
a,b = eval(input('Enter year and first day of year i.e. 0-Sunday,\
1-Monday,2-Tuesday,3-Wednesday,4-Thursday,5-Friday,6-Saturday :'))
Day = 'Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday\n'
print('January 1',a,'is',Day[b])
b=b+31
b=b%7
print('Feburary 1',a,'is',Day[b])
if (a % 4 == 0 and a % 100 !=0) or (a % 400 ==0):
    b=b+29
    b=b%7
    print('March 1',a,'is',Day[b])
else:
    b=b+28
    b=b%7
    print('March 1',a,'is',Day[b])    
b=b+31
b=b%7
print('April 1',a,'is',Day[b])
b=b+30
b=b%7
print('May 1',a,Day[b])
b=b+31
b=b%7
print('June 1',a,'is',Day[b])
b=b+30
b=b%7
print('July 1',a,'is',Day[b])
b=b+31
b=b%7
print('August 1',a,'is',Day[b])
b=b+31
b=b%7
print('September 1',a,'is',Day[b])
b=b+30
b=b%7
print('October 1',a,'is',Day[b])
b=b+31
b=b%7
print('November 1',a,'is',Day[b])
b=b+30
b=b%7
print('December 1',a,'is',Day[b])