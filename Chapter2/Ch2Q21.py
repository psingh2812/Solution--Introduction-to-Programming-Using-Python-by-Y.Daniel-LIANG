m=eval(input('Enter monthly savings:'))
r=1+0.00417
m1=m*r
m2=(m+m1)*r
m3=(m2+m)*r
m4=(m3+m)*r
m5=(m4+m)*r
m6=(m5+m)*r
m6=int(m6*100)/100
print('Savings after six months:',m6)