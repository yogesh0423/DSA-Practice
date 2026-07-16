array = [1,2,3,4,5]
total = 0
min = array[0]
max = array[0]

for num in array:
  total += num
  if num < min:
    min = num
  if num > max:
    max = num 

max_sum = total - min
min_sum = total - max
print(max_sum, min_sum)
