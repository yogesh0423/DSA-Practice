#Check if the number is palindrom or not.

n = 1234
num = n 
result = 0
while num> 0:
  lastDigit = num % 10
  result = (result*10) + lastDigit
  num //= 10

print(n == result)


