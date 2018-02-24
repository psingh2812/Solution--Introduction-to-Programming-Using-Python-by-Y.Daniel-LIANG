a=eval(input('Enter no between 0-1000:'))
mod=a % 10
s=mod
a=a//10
mod=a%10
s=mod+s
a=a//10
mod=a%10
s=mod+s
print(s)