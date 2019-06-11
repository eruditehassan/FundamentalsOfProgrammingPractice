import re
def stringCompairson():
	string1 = input("Enter the first string: ")
	string2 = input("Enter the second string: ")
	if (len(string1)== len(string2)):
		print(string1, " is equal to ",string2)
	elif (len(string1)> len(string2)):	
		print(string1, " is greater than ",string2)
	elif (len(string1)< len(string2)):	
		print(string1, " is smaller than ",string2)

def stringSearching():
	no_of_lines = int(input("How many lines you want to enter: "))
	print("Enter ",no_of_lines," of text")
	line_text = []
	for i in range(no_of_lines):
		line = input()
		line_text.append(line)
	search_string = input("Enter search string: ")	
	for i in line_text:
		if search_string in i:
			print("Yes, the given string was found")
			break

def stringPalindrome():
	input_string = input("Enter the string: ")
	if input_string == input_string[::-1]:
		print("Yes, this string is a palindrome")
	else:
		print("No, this string is not a palindrome")

def password_strength():
	password = input("Enter you password to evaluate your score")
	points = 0
	if 8<=len(password)<16:
		points+=2
		if re.search(['A-Z','a-z'],password) and re.search(['0-9'],password):
			points+=3
		if re.search(['$,@,#'],password):
			points+=3
		if re.search(['a-z'],password) and re.search(['A-Z'],password):
			points+=2
		elif len(password)<8:
			print("The length of password is less than 8 characters, try a longer one")
		elif len(password)>=16:
			print("The length of password is greater than or equal to 16, try a shorter password")
		print("The strength of your password is ",points," out of 10 points")				


