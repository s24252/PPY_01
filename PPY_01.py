# task 1
name = input("Enter your name: ")
surname = input("Enter your surname: ")
age = input("Enter your age: ")
print("Name: ", name)
print("Surame: ", surname)
print("Age: ", age)
# task 2
fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print("Temerature in Celcius: ", celsius)
#task 3
score = float(input("Enter your score: "))

if score >= 90:
    grade = "5"
elif score >= 80:
    grade = "5"
elif score >= 70:
    grade = "4"
elif score >= 60:
    grade = "4"
elif score >= 50:
    grade = "project"
elif score >= 30:
    grade = "test"
elif score >= 20:
    grade = "work in class"
else:
    grade = "2"

print("Your grade is:", grade)
# task 4
number = int(input("Enter a number: "))
number2 = int(input("Enter second number"))

if number % number2 == 0:
  result = "diveded"
else:
  result = "not devided"
print("The number is", result)
#task 6 (corrected)
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
is_triange = "true";

if side1 + side2 > side3 or side1 + side3 > side2 or side2 + side3 > side1 :
    is_triange = "false"
elif side1 <= 0 or side2 <= 0 or side3 <= 0:
    is_triange = "false"
else:
    if side1 == side2 == side3:
        triangle_type = "Equilateral"
        print("The triangle is:", triangle_type)
    elif side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
        print("The triangle is:", triangle_type)
    else:
        triangle_type = "Scalene"
        print("The triangle is:", triangle_type)

print("Is triangle: ", is_triange)

#task 7
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
      result = "Invalid operation"
    else:
      result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)