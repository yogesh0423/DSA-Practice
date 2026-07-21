# Ask the user to enter a number between 1 and 10 and print a corresponding prize using match case.
a= int(input("enter a number between 1 and 10 :"))

match a :
    case 1:
        print("you won a charger")
    case 3:
        print("you won a chocolate")
    case 5:
        print("you won a camera")
    case _:
        print("better luck next time")


# Ask the user to enter two numbers and an operator (+, -, *, /) and perform the corresponding operation using match case.
n = int(input())
m = int(input())

operation = input("Enter the operator:")

match operation :
    case "+":
        print(n + m)
    case "-":
        print(n - m)
    case "*":
        print(n * m)
    case "/":
        print(n / m)


# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
n = int(input("Enter a number between 1 to 7: "))

match n :
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    

