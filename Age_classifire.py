#  Write a program that takes an age as input and prints a message based on the following 
# 1. Age Classifier 
''' age = int(input("Enter your age Pallavi: "))

if(age < 12):
    print("You are a child." )
elif(age > 12 and age < 17):
    print("You are a teenager." )
elif(age > 18 and age < 64):
    print("You are an adult." )
else:
    print("You are a senior citizen.") '''


# 2. Number Classification
''' number = int(input("Enter the number : "))

if(number == 0):
    print("The number is zero" )
elif(number < 0 ):
    print("The number is negative" )
else:
    print("The number is positive" )'''

# 3. Leap Year Checker 
'''year = int(input("Enter a year to check if it is a leap year or Not: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''

# 4. Grade Calculator : Write a program that takes a score as input (0–100) and prints the corresponding grade:
''' score = int(input("Enter your grade : "))
if(score >= 90):
    print("Grade A" )
elif(score >= 80 & score < 90):
    print("Grade B")
elif(score >= 70 & score < 80):
    print("Grade C")
elif(score >= 60 & score < 70):
    print("Grade D" )
else:
    print("Fail") '''

# 5. Odd or Even 
''' num = int(input("Enter the number : "))
if(num == 0 or num % 2 == 0):
    print("The number is even")
else:
    print("The number is odd" ) '''


# 6. Maximum of Three Numbers : Write a program that takes three numbers as input and prints the largest one. 

''' num_1 = int(input("Enter first the number : "))
num_2 = int(input("Enter second the number : "))
num_3 = int(input("Enter third the number : "))

if(num_1 > num_2 & num_1 > num_3):
    print("num_1 is greater")

elif(num_1 < num_2 & num_2 > num_3):
    print("num_2 is greater")
else:
    print("num_3 is greater") '''


# 7. Login Authentication : Write a program 
'''
Username = input("Enter your Username : ")
password = int(input("Enter your password : "))

if(Username == 'admin' and password == 1234):
    print( "Login successful." )
else:
    print("Enter valid username and password") '''


# 8. Triangle Validator
'''side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
    print("The sides form a triangle.")
else:
    print("The sides do not form a triangle.")'''

# 9. Traffic Light Guide :  Write a program that takes a traffic light color as input (red, yellow, or green) and prints:

'''sign = input("Enter the traffic light color  : ")

if(sign == 'red'):
    print('the signal is red stop!')
elif(sign == 'yellow'):
    print('the signal is yellow, Get ready!')
elif(sign == 'green'):
    print('the signal is green, Go..')
else:
    print("Invalid traffic light color.")'''

# 10. BMI Calculator 
'''weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

# Compute BMI
bmi = weight / (height ** 2)

# Print BMI category
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("Category: Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Category: Normal weight")
elif 25 <= bmi <= 29.9:
    print("Category: Overweight")
else:
    print("Category: Obese")'''
# Assignment done by Pallavi Bhasme