
# Count the number of vowels in the string "Coding in Python is fun" and print the result.
sentence = "Coding in Python is fun"
sum = 0
vowels = ['a', 'e', 'i', 'o', 'u']

for char in sentence:
    if char in vowels:
        sum += 1

print(f"The number of vowels in the sentence is: {sum}")

