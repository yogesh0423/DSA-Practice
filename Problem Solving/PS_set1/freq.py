str = input()
char = input()

str_list = list(str)

count = 0

for letter in str:
    if char == letter:
        count+= 1
print(count)
