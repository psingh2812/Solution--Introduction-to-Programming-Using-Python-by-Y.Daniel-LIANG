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
    
    
    def __str__(self):
        return 'id='+str(self.__aid)+' balance='+str(self.__balance)+\
            ' Monthly interest rate='+str(self.getMonthlyInterestRate())\
            +' Interest Rate='+str(self.__AIR)    
def main():
    accounts = []
    for i in range (10):
        accounts.append(Account(i,100,4.5))
        
    while True:
        ids = eval(input('Enter an account id:'))    
                    
        while (0 <= ids < 10):
            print('Enter a valid id between 0 and 9')
            
        
            acc = accounts[ids]
    
            print('Main Menu:')
            print('1:Check balance')
            print('2:Withdraw')
            print('3:Deposit')
            print('4:Exit')
    
            choice = eval(input('Enter a choice:'))
            if choice ==1:
                print('The balance is '+str(acc.bal_accessor()))
        
        
            elif choice ==2:
                amount = eval(input('Enter an amount to withdraw:'))
                acc.withdraw(amount)
        
            elif choice ==3:
                amount = eval(input('Enter an amount to deposit:'))    
                acc.deposit(amount)
    
            elif choice == 4:
                break 
                       

main()            
                        
                        
            