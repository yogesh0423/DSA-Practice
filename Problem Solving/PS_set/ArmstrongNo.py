n = int(input())
num = n 
total = 0
digit = len(str(n))
while num > 0:
    last_digit = num % 10
    total = total + (last_digit**digit)
    num = num // 10
    
print("The given number is armstrong:",total == n)
