# ticket machine printing numbers in reverse order 

num = int(input())
digits = 0
reverse = 0
while num > 0:
    digits = num %10
    reverse = reverse * 10 + digits
    num = num // 10
print(reverse)
