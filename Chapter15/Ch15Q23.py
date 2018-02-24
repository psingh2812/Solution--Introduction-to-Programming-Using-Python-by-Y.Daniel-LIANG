def displayPermutations(s):
    displayPermutationhelper('',s)    
    
        
def displayPermutationhelper(s1,s2):
    if len(s2) == 0:
        print(s1)
        return
    for index,letter in enumerate(s2):
        
        #print('12',s2[0:index])
        #print('13',s2[index+1:])
        new_s2 = s2[0:index] + s2[index+1:]
        #print(new_s2)
        new_s1 = s1 + letter
        #print('2',new_s1)
        
        displayPermutationhelper(new_s1,new_s2)
    
def main():
    s1 = input('Enter String')
    displayPermutations(s1) 
    
main()    
    