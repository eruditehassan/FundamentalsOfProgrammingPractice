def starHalfTriangle():
	"""A program that prints half star triangle"""
	no_of_stars = 0
	for stars in range(1,13):
	    no_of_stars+=1
	    print(no_of_stars * '*')

def customStarFormat():
	"""A program that reads a number (between 1 and 30) and print a line containing that number of adjacent asterisks using for loop"""	 
	number=int(input("How many asterisks you want to print? Enter a number between 1 and 30 \n"))
	if 1 <= number <=30:
	    print(number * '*')
	else:
	    print ("Number is not between 1 and 30")

def primeNumber():
	"""A program to check whether a number entered by a user is a prime number or not"""
	number = int(input("Enter any number"))
	no_of_factors = 0
	if number > 1:
	    for test in range(1,number+1):
	        if number%test==0:
	            no_of_factors+=1
	if no_of_factors ==2:
	    print("Yes, it is a prime number")
	elif no_of_factors > 2:
	    print("No, it is not a prime number")

def customNumPrintLoop():
	"""A loop that prints out all  numbers between 6 and 30 that are not divisible by 2, 3, and 5."""   
	for number in range(6,31):
	    if not(number%2==0 or number%3==0 or number%5==0):
	        print(number)

def cityListPrinter():
	city_names = ['Karachi', 'Lahore', 'Islamabad', 'Istanbul', 'Melbourne', 'Paris', 'Berlin',  'London']
	num = 0
	for cities in city_names:
	    num +=1
	    print (num,".",cities)

def interestCalculator():
	"""The program computes the interest accumulated on an account"""
	principal=0
	print("This program calculates the future value of investment for any number of years.")
	principal = eval(input("Enter the initial principal amount: "))
	apr = eval(input("Enter the annual interest rate: "))
	years = int(input("Enter the number of years to calculate investment"))
	for i in range(years):
	         principal = principal * (1 + apr)
	print ("The value in", years, "years is:", principal)    

def powerSequenceGenerator():
	print("This program will calculate square, cube and fourth power of numbers from 1 to any number you give")
	number = int(input("Enter the number uptil which you want to calculate"))
	print("n \t n^2 \t n^3 \t n^4")
	n = 0
	for calculation in range(number):
	    n+=1
	    print(n, '\t', n**2, '\t', n**3, '\t', n**4)
