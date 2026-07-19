
# Print numbers from 1 to 10 using a while loop.
i = 1

while i < 11:
    print(i)
    i += 1


# Calculate the sum of numbers from 1 to 100 using a while loop.
sum = 0
i = 1

while i <= 100:
    sum += i
    i += 1

print(sum)


# Write a program that keeps asking the user to enter a password until they enter the correct one.
password = "YK234"
entered_pass = input("Enter password: ")

while (entered_pass != password):
    entered_pass = input("Wrong password! Try again and enter password: ")
    
print("Success! You ara logged in")


# Use a while loop to reverse a given number (e.g., 123 → 321).

number = int(input("Enter a number to reverse: "))

while number > 0:
    digit = number % 10
    print(digit, end="")
    number //= 10
