class Stack(list):
    def __init__(self):
        super().__init__()
        
    def isEmpty(self):
        if len(list.copy(self)) == 0:
            return True
        else:
            return False
        
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return super().copy()[len(list.copy(self))-1]
        
    def push(self,value):
        super().append(value)
        
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return super().pop(len(list.copy(self))-1)
        
    def getSize(self):
        return len(list.copy(self))
    
    def __str__(self):
        return super().__str__()
    
def main():
    strings = input('Enter five strings:').split() 
    st = Stack()
    
    for i in range (len(strings)):
        st.push(strings[i])
    print('Original stack-> ',st) 
    print(st.pop())
    print(type(st.pop()))
    
    st.reverse()   
    print('Reverse stack-> ',st)
    
    
main()    
        
                       
            