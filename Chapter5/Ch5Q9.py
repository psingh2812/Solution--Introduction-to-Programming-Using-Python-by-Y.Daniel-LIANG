#Q.No9 Calculating tuition fee
t= 10000
r = 0.05
i,tot,t2,t3,t4 = 0,0,0,0,0
while(i< 10):
    t =  t*(1+r)
    t2 = t*(1+r) 
    t3 = t2*(1+r)
    t4 = t3*(1+r)
    tot = t+t2+t3+t4
    print('Tuition in Year',i+1,'from now:$',format(t,'.2f'))
    print('Tuition cost for four years in Year',i+1,'from now:$',format(tot,'.2f'))
    i = i+1