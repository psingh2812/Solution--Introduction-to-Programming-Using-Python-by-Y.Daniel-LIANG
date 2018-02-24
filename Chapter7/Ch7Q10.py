import datetime
class Time:
    def __init__(self,hr,mn,sc):
        self.__hr = hr
        self.__mn = mn
        self.__sc = sc
        
    def gethr(self):
        return self.__hr  
    
    def getsec(self):
        return self.__sc
    
    def getmin(self):
        return self.__mn
    
    def SetTime(self,elpt):
        day = elpt//(60*60*24)
        elpt = elpt - day * 86400
        hr =  elpt//(60*60)
        elpt = elpt - hr*3600
        mn =  elpt//60
        elpt = elpt - (mn*60)
        sec = elpt
        self.__hr = hr
        self.__mn = mn
        self.__sc = sec
        
def main():
    now = datetime.datetime.now()
    t = Time(now.hour,now.minute,now.second)
    print('Current Time:',now)
    et = eval(input('Enter elapsed time:'))
    t.SetTime(et)
    print('The hour:minute:second for elapsed time is:',t.gethr(),':',t.getmin(),':',t.getsec())
    
main()
    
    
    
    
    
    
    
    
    
     