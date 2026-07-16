
def fact(n):
    if n== 1:
        return 1
    else:
        return n* fact(n-1)
    
num = int(input())
originalNum = num 
total = 0
while(num!= 0):
    digit = num %10
    total = total + fact(digit)
    num = num//10
if total == originalNum:
    print("Yes, Strong")
else:
    print("No")