# Extraction of digits of an integer

n = 5678
num = n
while num > 0:
  digit = num % 10
  print(digit)
  num //= 10
