
def sumCalculator():
	"""#A program that asks the user about the number of values he/she wants to enter.
	Then prompt user to enter the values as per the required number, calculate its sum"""
	while True:
    values = int(input("How many values you want to enter?"))
    num_list = []
    for inputs in range(values):
        numbers = int(input("Enter the number:"))
        num_list.append(numbers)
    print("The sum of the given numbers is", sum(num_list))
    if (input("Do you want to repeat the program? (y / n)").lower() == 'n'):
        break


def factorialCalculator():
	"""A program that accepts an integer from the user and displays its factorial"""
	while True:
	    fact_num = int(input("Enter any number to calculate its factorial:"))
	    import math
	    print ("The factorial of", fact_num, "is", math.factorial(fact_num))
	    if (input("Do you want to repeat the program? (y/n)").lower() == 'n'):
	        print("Thank you for using the program")
	        break


def numberGuessing():
	"""A program that plays a simple number-guessing game. The user will try to guess the secret number until they get it right"""
	while True:
    from random import randint
    secret_number = randint(1,10)
    print("I have chosen a number between 1 and 10. Try to guess it")
    guess = int(input("Your guess:"))
    while guess !=secret_number:
        guess = int(input("Your guess:"))
        if guess == secret_number:
            print("Your guess is right!")
            break
    repeat = input("Do you want to guess again? (y/n)").lower()
    if repeat == 'n':
        print("Thank you for playing")
        break

def incomeSupport():
	"""An Income Support program follows the following mentioned rules to determine the income support package. 
	(1) If a person’s health is excellent and the person is between 25 and 35 years of age and lives in a city and is a male then the maximum monetary amount awarded is Rs. 2 lakhs.
	(2) If a person satisfies all the above conditions except that the gender is female then the maximum monetary amount awarded is Rs. 1 lakh.
	(3) If a person’s health is poor and the person is between 25 and 40 years of age and lives in a village and is a male then the maximum amount awarded is Rs. 5 Lakh.
	(4) In all other cases the person is not eligible for the income support program."""

	while True:
    health = int(input("Your health condition: \n 1. Excellent \n 2. Poor \n"))
    age = int(input("What is your age? (In numbers)"))
    locality = int(input("Where do you live? \n 1. City \n 2. Village\n"))
    gender = int(input("What is your gender? \n 1. Male \n 2. Female\n"))
    if (25 <= age <= 35):
        print("You're eligible for the income support program")
        if (health == 1) and (25 <= age <= 35) and (locality == 1) and (gender == 1):
            print ("The maximum monetary amount that could be awarded to you is Rs. 2 Lakh")
        elif (health == 1) and (25 <=age <= 35) and (locality == 1) and (gender == 2):
            print("The maximum monetary amount that could be awarded to you is Rs. 1 lakh")
    if (health == 2) and  (25 <= age <= 40) and (locality == 2) and (gender == 1):
            print("The maximum monetary amount that could be awarded to you is Rs. 5 Lakhs")    
    else:
        print("You're not eligible for the income support program")
    if (input("Do you want to check again? (y/n)").lower() == 'n'):
        print ("Thank you for using the program")
        break

def genderGame():
	"""A Program which displays an appropriate name for a person, using a combination of nested ifs and compound conditions. Ask the user for a gender, first name,
	last name and age. If the person is female and 20 or over, ask if she is married. If so, display "Mrs." in front of her name. If not, display "Ms." in front of her name. If the female is under 20, display her
	first and last name. If the person is male and 20 or over, display "Mr." in front of his name. Otherwise, display his first and last name."""
	while True:
    gender = int(input("What is your gender: \n 1. Male \n 2. Female\n"))
    first_name = input("Enter your first name:\n")
    last_name = input("Enter your last name:\n")
    age = int(input("Enter your age:\n"))
    if (gender == 2) and (age >=20):
        married = input("Are you married? (y/n)").lower()
        if married =='y':
            print ("Mrs.", first_name, last_name)
        else:
            print ("Ms.", first_name, last_name)
    elif (gender ==2) and (age < 20):
        print(first_name, last_name)
    if (gender == 1) and (age >= 20):
        print ("Mr.", first_name, last_name)
    elif (gender ==1) and (age < 20):
        print(first_name, last_name)
    if (input("Do you want to check again? (y/n)").lower() == 'n'):
        print("Thank you for using the program")
        break



