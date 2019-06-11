def coordinatePrinter():
	row = int(input("Enter the number of rows: "))
	column = int(input("Enter the number of Columns: "))
	for row_items in range(row+1):
	    for column_items in range(column+1):
	        print("(",row_items,",",column_items,")", end="  ")
	    print()    

def pythagoreanTriples():
	"""A right triangle can have sides that are all integers. The set of three integer values for the sides of a right triangle is called a Pythagorean triple. 
	These three sides must satisfy the relationship that the sum of the squares of two of the sides is equal to the square of the hypotenuse. 
	Find all Pythagorean triples for side1, side2, and the hypotenuse all no larger than 500. """
	counter = 0
	for side1 in range(1,501):
	    for side2 in range(1,501):
	        for side3 in range(1,501):
	            if side3**2 == side1**2 + side2**2:
	                print(side1,side2,side3)
	                counter +=1
	print("The number of such triples found is:",counter)

def grading():
    score = int(input("Enter your score (0 - 100):"))
    if 0 <= score <= 100:
        if score >= 90:
            print ("Your grade is A")
        elif 80 <= score <= 89:
            print ("Your grade is B")
        elif 70 <= score <= 79:
            print ("Your Grade is C")
        elif 60 <= score <= 69:
            print ("Your Grade is D")
        elif score <= 59:
            print ("Your Grade is F")
    else:
        print ("Invalid Input")

def converter():
	"""A program that consists of the following conversion functions:
	 1. Miles to Km converter
	 2. Celsius to Fahrenheit converter
	 3. ft. to meters converter
	 4. Yards to meters converter

	"""
	decision = 0
	while decision !=-1:
	    def miles_to_km():
	        miles = int(input("Enter the number of miles:"))
	        if miles >= 0:
	            kilometer = 1.60934*miles
	            print(miles, "miles are equal to", kilometer, "kilometers")
	        else:
	            print ("Invalid Input, enter a positive")
	    def celcius_to_fh():
	        celcius = int(input("Enter the temperature in Celcius:"))
	        fahrenheit = 1.8*celcius + 32
	        print ("Temperature in Fahrenheit is",fahrenheit)
	    def feet_to_meters():
	        feet =int(input("How many ft.?"))
	        if feet >= 0:
	            meters = 0.3048 * feet
	            print("Length in meters is", meters)
	    def yards_to_meters():
	        yards =int(input("Enter the length in yards:"))
	        meters_from_yards = 0.9144 * yards
	        print ("The length in meters is", meters_from_yards)
	    decision = int(input("Which conversation do you want to make (Enter -1 to end the program)\n 1. Miles to Kilometers \n 2. Celcius to Fahrenheit \n\
	 3. Feet to Meters \n 4. Yards to Meters\n"))
	    def function_call():
	        if decision == 1:
	            miles_to_km()
	        elif decision ==2:
	            celcius_to_fh()
	        elif decision ==3:
	            feet_to_meters()
	        elif decision ==4:
	            yards_to_meters()
	        elif decision ==-1:
	            print("The program is exiting, you've entered the sentinal value")
	        else:
	            print("Invalid input")
	    function_call()
