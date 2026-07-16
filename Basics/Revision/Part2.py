------Even Odd------
n = int(input())
if n % 2 == 0:
  print("Even")
else:
  print("Odd")
  
------Largest of three------
a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
  print("a is largest elem")
elif b > a and b > c:
  print("b is largest elem")
elif c > a and c > b:
  print("c is largest elem")
