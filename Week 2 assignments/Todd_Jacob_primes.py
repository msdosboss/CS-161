import math 
flag=True
y = int(input())
x=2
while x < y and flag==True:
    z = y % x
    if z==0:
        flag=False
    x=x+1
if flag == False:
    print(y,"is not a prime number")
else:
    print(y,"is a prime number")