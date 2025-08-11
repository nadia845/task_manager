"""# Request user to input their name
name = input("what is your name?: ")
print(name)
# print welcome message with user's name
# print("welcome, " + name + " to GROWC6 at Buro.")

# string formatting

#print(f("Welcome, {}"))


# If condition
age = input("How old are you?\n")
if int(age) >= 18 and int(age) >= 45:
    print("You have acess.")
else:
    print("You are not allowed")

    # Ask user to input an integer
    number = input("type in an integer.\n")
    # Determine the modulo of the integer
    if int(number) % 2 == 0:
      print("It is even")
    else:
       print("It is odd") """
    # If modulo is equal to 2 print even
    # Else print odd

    # Ask user to input their score as number 
"""number = int(input("input your score.\n"))
    # If score is between 90 to 100(inclusive) print grade A
if number >=90:
    print(f"{number} is grade A")
    # If score is between 80 to 89 (iclusive) print grade B
if number >=80 and (number) <=89:
     print(f"{number} is grade B")
    # if score is between 70 to 79(inclusive) print grade C
if number >=70 and (number) <=79:
    print(f"{number} is grade C")
    # if score is between 60 to 69(inclusive) print grade D
if number >=60 and (number)  <=69:
    print(f"{number} is grade C")
    # if score is between 0 to 59(inclusive) print grade F 
if number >=0 and (number) <=59:
    print(f"{number} is grade F")"""


# discount calculator
# Ask user to input their purchase amount as float
# If the purchase is 100 cedis or more apply 20% discount and print amount to pay
purchase_amount = float(input("Enter price of the item: "))
if purchase_amount >= 100:
    discount_1 = (20/100)*(purchase_amount)
    discount_price1 = purchase_amount - discount_1
    print(f"There is 20% discount. so instead of paying{purchase_amount},you will pay Gh{discount_price1}")
# if the purchase is 50 cedis or more apply 10% discount and print amount to pay
elif purchase_amount >= 50:
    discount_2= 10/100 *(purchase_amount)
    discount_price2 = purchase_amount - discount_2
    print(f"There is a 10% discount. so instead of paying {purchase_amount}, you will pay Gh{discount_price2}")
# if the purchase is less than 50 cedis apply no discount and print amount to pay
else:
    print(f"Since your total purchase is less than 50, you do not have any discount. you are to pay Gh{purchase_amount}")


# program to calculate the average of two numbers
"""num1 = int(input("Enter number1. "))
# take two numbers as input
num2 = int(input("Enter number2. "))
# declare the average variable
result = (num1 + num2) /2
# declare average = (num1 + num2) / 2
print(f"the average of the two numbers is {result}")
# display the average
# ALTERNATIVELY......
num1= float(input("Enter first number: "))
num2= float(input("Enter second number: "))
print(f"The average of {num1} and {num2} is {(num1 +num2) / 2}")"""

# accept an age input from the user and a fullname
"""name = input("Enter your fullname: ")
age = int(input("Enter your age: "))
if (age < 18) and (result == 20):
    print(f"{name}, you are not allowed to vote.")
# if the age is less than 18 and the average is equal to 20, 
# print {name}, you are not allowed to vote
if (age < 18) and (result == 20):
    print(f"{name}, you are not allowed to vote.")
# if the age is greater than or equal to 18 and the average is
# greater than or equal to 20, print{name}, you are allowed to vote
# if the age is greater than or equal 
if (age >= 18) and (result >= 20):
    print(f"{name}, you are allowed to vote.")"""




# Ask your user to input the length of the 3 sides of a triangle
x = float(input("Enter the first side: "))
y = float(input("Enter the second side: "))
z = float(input("Enter the third side: "))
# if all sides are equal print Equilateral
if x == y and y == z:
    print("The triangle is Equilateral")
elif x == y or y == z or x == z:
    print("isosceles")
# if no sides are equal prnt scalene
else:
    print("scalene")


