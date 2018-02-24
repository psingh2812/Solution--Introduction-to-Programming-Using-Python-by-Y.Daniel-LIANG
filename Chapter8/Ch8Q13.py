def prefix(s1,s2):
    s = str()
    if(s1[0]==s2[0]):
        l1 = len(s1)
        l2 = len(s2)
        if(l1>=l2):
            
            for i in range (l2):
                if(s1[i]==s2[i]):
                    s = s+s1[i]
        else:
            for i in range (l1):
                if(s2[i]==s1[i]):
                    s = s+s1[i]         
        
        return(s)
    
        
    else:
        return(s) 


def main():
    string1 = input('Enter string1:') 
    string2 = input('Enter string2:') 
    ans = prefix(string1,string2)
    if(len(ans)==0):
        print('No prefix found') 
    else:
        print('Prefix is:',ans)    
        
main()        