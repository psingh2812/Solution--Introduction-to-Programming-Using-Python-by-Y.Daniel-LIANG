

def check_safe(lst):
   
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if abs((lst[j]-lst[i])*1.0/(j-i))==1:
                return False
    return True

def print_solution(lst):
    
    for i in range(len(lst)):
        stars=['.']*len(lst)
        stars[lst[i]]='Q'
        print (stars)

def list_mutation(n):
    
    if n==0: yield [n]
    else:
        for lst in list_mutation(n-1):
            for i in range(n):
                yield lst[0:n-1-i]+[n-1]+lst[n-1-i:n-1]
                
def queens(n):
    
    print ("N queens solution")
    for q in list_mutation(n):
        if check_safe(q):
            yield q
            break
        

def main():

    N=8
    for q in queens(N):
        print_solution(q)

main()