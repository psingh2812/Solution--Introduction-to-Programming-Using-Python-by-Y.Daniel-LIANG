def merge(l1,l2):
    m = []
    c1 = 0
    c2 =0
    
    while c1<len(l1) and c2 < len(l2):
        if l1[c1]<l2[c2]:
            m.append(l1[c1])
            c1 +=1
        else:
            m.append(l2[c2])
            c2 +=1
            
            
    while c1 < len(l1):
        m.append(l1[c1])
        c1 =+1
        
    return m    

def main():
    l1 = input('Enter list1:').split()
    l2 = input('Enter list2:').split()
    n1 = [eval(x) for x in l1]
    n2 = [eval(x) for x in l2]
    print(n1)
    print(n2)
    
    n1.sort()
    n2.sort()
    n3 = merge(n1,n2)
    
    print('The merged list is:',n3)
    
main()    
                    