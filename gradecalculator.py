# grade = int(input("What is your grade percent? "))

# if grade >= 90:
#     letter = "A"
# elif grade >= 80:
#     letter = "B"
# elif grade >= 70:
#     letter = "C"
# elif grade >= 60:
#     letter = "D"
# else:
#     letter = "F"

# print(f"Your letter grade is: {letter}")

# if grade >= 70:
#     print("Congratulations! You passed the class!")
# else:
#     print("Stay focused and you'll get it next time!")

# grade = int(input("What is your grade percentage? "))
 
# Determine the letter grade
# if grade >= 90:
#     print("You will receive an A")
# elif grade >= 80:
#     print("You will receive a B")
# elif grade >= 70:
#     print("You will receive a C")
# elif grade >= 60:
#     print("You will receive a D")
# else:
#     print("You will receive an F")
 
# # Determine if the grade is passing
# Passing_grade = grade >= 70
 
# # Print the result based on whether the grade is passing
# if Passing_grade:
#     print("Congratulations, you passed!")
# else:
#     print("Please retake the course, we know you can ace it next time!")
 
# # Assign the sign based on specific ranges
# sign = ""
# if grade == 100:
#     sign = "+"
# elif 90 <= grade <= 94:
#     sign = "-"
# elif 80 <= grade < 90:
#     sign = "+"
 
# # Output the grade and the sign
# print(grade)
# print(sign)

country = 'CANADA'
country = input('Where are you from? ')
if country.lower() == 'canada':
    print('Oh look a canadian')
else:
    print('you are not from canada')


price = input('How much is your salary? ')

price = float(price)
if price >= 25000.00:
    tax =   .09
elif price == 10000.00:
    tax = .03
elif price <= 9000.00:
    tax = .01
    print('tax rate is: ' + str(tax))
else:
    tax = 0
    print('tax rate is: ' + str(tax))