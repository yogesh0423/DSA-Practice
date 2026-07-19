'''
Create a string variable name with your full name. 
Print:
    The first character
    The last character
    The length of the string
'''

str = "Yogesh"
print(str[0])
print(str[-1])
print(len(str))


# Concatenate two strings: "Hello" and "World" with a space in between.
str1 = "Hello"
str2 = "World"
print( str1 + str2)


# Create a string variable called "text" with the value "Python Programming".
text = "Python Programming"

print(text[0:6])
print(text[-6:])
print(text[::2])

# Reverse the string "Python Programming" using slicing and print the result.
text = "Python Programming"
print(text[::-1])


# Create a string variable called "str3" with the value " i love python programming ".
str3 = " i love python programming "
 
print(str3.strip())
print(str3.title())
print(str3.count("o"))
 

# Check if the string "123abc" is alphanumeric (contains only letters and numbers) and print the result.
str4 = "123abc"
print(str4.isalnum())


# Create a string variable called "sentence" with the value "Coding in Python is fun".
sentence = "Coding in Python is fun"

print(sentence.replace("fun", "awesome"))
print(sentence.index("Python"))
print(sentence.upper())

