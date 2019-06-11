#A program that reads an integer and determines and prints whether it is odd or even
def oddEvenChecker():
	num = int(input("Enter a number to check whether it is even or odd"))
	if (num%2 == 0):
		print("Number is Even")
	else:
		print("Number is Odd")	

#A program that inputs three different integers from the keyboard, and then prints the smallest and the largest of these numbers
def largestSmallestChecker():
	numbers =[]
	repitition = int(input("How many numbers you want to enter?"))
	for i in range(repitition):
		a = int(input("Enter a number:"))
		numbers.append(a)
	print("The largest number is %d"%max(numbers))
	print("The smallest number is %d"%min(numbers))	

#Taking three non-negative integers and determining if they are sides of a traiangle
def triangleSides():
	side1 = int(input("Enter the first side"))
	side2 = int(input("Enter the second side"))
	side3 = int(input("Enter the third side"))
	if (side1 >= 0 and side2>= 0 and side3>=0):
		if ((side1**2 == side2**2 + side3**2) or (side2**2 == side1**2 + side3**2) or (side3**2 == side1**2 + side2**2)):
			print("Yes, these are sides of a triangle")
		else:
			print("No, they are not sides of a traingle")
	else:
		print("Sides can not be negative")			

#A program that reads an integer and determines whether or not it is a palindrome. 
def palindromeNumber():
	number = input("Enter the number to check whether it is a palindrome: ")
	if number == number[::-1]:
		print("Yes, the number is a palindrome")
	else:
		print("No, the number is not a palindrome")

#A program that takes as input a letter and displays if it is a vowel using conditional statements
def vowelChecker():
	vowels = ['a','e','i','o','u']
	letter = input("Enter an alphabet to check if it is a vowel or not: ")
	if letter in vowels:
		print("Yes, the given letter is a vowel")
	else:
		print("It is not a vowel")	

def electricBillCalculator():
	units  = int(input("Enter the number of units consumed: "))		
	if (units<=200):
		bill = units * 1.5
	elif (200<units<=300):
		bill = units * 3.5
	elif (300<units<=600):
		bill = units * 4.5
	elif (units>600):		
		bill = units * 5.5
	print("The Electric Bill is %.3f"%bill)	