def main():
    s1 = input('Enter sub string:')
    s2 = input('Enter string :')
    s = fsub(s1,s2)
    if(s):
        print(s1,'is a substring in',s2)
    else:
        print(s1,'is not a substring in',s2)    
    


def fsub (sub,st):
    l1 = len(st)
    l2 = len(sub)
    Subs = False
    for i in range(0,l1):
        if (sub[0]==st[i]):
            for j in range(0,l2):
                if (sub[j] == st[j+i]):
                    Subs = True
                else:
                    Subs = False
                    break
            if (Subs == True):
                return(Subs)

    return(Subs)



main()