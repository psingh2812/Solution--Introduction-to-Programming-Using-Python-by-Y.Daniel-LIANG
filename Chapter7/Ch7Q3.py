class Account:
    def __init__(self,aid=0,balance=100,AIR=0):
        self.__aid=aid
        self.__balance=balance
        self.__AIR=AIR
        
    def mutator (self,new_aid,new_balance,new_AIR):
        self.__aid = new_aid
        self.__balance = new_balance
        self.__AIR = new_AIR
        
    def aid_accessor(self):
        return self.__aid
    
    def bal_accessor(self):
        return self.__balance
    
    def AIR_accessor(self):
        return self.__AIR
    
    
    def getMonthlyInterestRate(self):
        return self.__AIR/1200
    
    def getMonthlyInterest(self):
        return self.getMonthlyInterestRate()*self.__balance
    
    def withdraw(self,wamt):
        self.__balance -=wamt
        
    def deposit(self,damt):
        self.__balance +=damt
    
    def display(self):
        print('Account ID:',self.aid_accessor())
        print('Balance:',self.bal_accessor())
        print('Montly Interest Rate:',self.getMonthlyInterestRate())
        print('Monthly interest:',self.getMonthlyInterest(),'\n\n')    
        
        
def main():
    a1 = Account(1122,20000,4.5)
    a1.display()
    
    a1.withdraw(2500)
    a1.display()
    
    a1.deposit(3000)
    a1.display()
    


main()
                 
        
    
        
           
        