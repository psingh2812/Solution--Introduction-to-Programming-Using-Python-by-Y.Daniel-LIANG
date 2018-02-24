def dev(x):
    s = 0
    lst = []
    lst.append(mean(x))
    
    for i in range(len(x)):
        s +=(x[i]-lst[0])**2
    lst.append((s/(len(x)-1))**0.5)    
    
    return lst

def mean(x):
    s = 0
    for i in range(len(x)):
        s +=x[i]
    return s/len(x)


def main():
    
    s = input('Enter numbers separated by space:').split()
    n = [eval(x) for x in s]
    ans = dev(n)
    
    print('The mean is:',round(ans[0],2))
    print('The S.D is:',round(ans[1],2))
    
main()
    
        
    