#Q.No26 Summation of series
i,s = 1,0
n = eval(input('Enter last odd numerator till you want summation of series : \n1/3\
+ 3/5 + 5/7 + 7/9 .....'))
while(i<n+1):
    s = s+i/(i+2)
    i=i+2
print(format(s,'.2f'))   