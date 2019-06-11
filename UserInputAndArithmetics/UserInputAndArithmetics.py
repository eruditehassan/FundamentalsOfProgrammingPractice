#First Example, having two values and using print statement
def twoValues():
	x=3
	y=12.5
	print ("The rabbit is", x)
	print("The rabbit is", x , "years old")
	print (y, "is average.")
	print(y,"*",x)
	print("12.5*3 is", x*y)

#A program that prompts the user to input two values. Assign user defined values to two variables and then swap their values. 
def valueSwap():
	first_value=float(input("Enter first value"))
	second_value=float(input("Enter second value"))
	first_placeholder = first_value
	second_placeholder = second_value
	first_value = second_placeholder
	second_value = first_placeholder


