#Q.No11 Student records
n = eval(input('Enter number of students:'))
h1,h2,i=0,0,0
while(i<n):
    s = eval(input('Enter score for Student'+str(i+1) +' :'))
    if(s>h1):
        h2=h1
        h1=s
    i=i+1

if (s>h2 and s<h1):
    h2 = s


        
if(n==0):
    print('No records entered')
elif(n==1):
    print('Only one record entered,Highest score is:',format(h1,'.2f'))  
else:
    print('Total no of records entered are:',n)
    print('Highest score is :',format(h1,'.2f'))
    print('Second highest score is:',format(h2,'.2f'))
          
        
        