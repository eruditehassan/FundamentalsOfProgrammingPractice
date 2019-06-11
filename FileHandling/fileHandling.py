def numOfLinesAndWordsCounter():
	#Store the file in the same directory as the program
	file = open('Test.txt','r')
	line_counter = 0
	for line in file:
	    #print(line)
	    line_counter +=1
	#seeking back to zero position to read from start    
	file.seek(0)
	word_counter = 0
	for words in file.read().split():
	    word_counter+=1
	print("The number of lines are", line_counter)
	print("The number of words are", word_counter)
	file.close()

def file_search_with_count(file_name,search_term):
	#Make sure that the file is in the same directory as the program
	#If it is not in same directory then specify complete path
    file = open(file_name,'r')
    count = file.read().lower().count(search_term.lower())
    #Lowercasing both the strings to avoid any mistake due to upercase lowercase mismatch
    if count>0:
        print("Yes, the given term appears in the file", count, "times")
    else:
        print("The term was not found in the given file")

from random import *
def hundred_random():
	#File should be in the same directory as the program
	file = open("100 random.txt", "w")
	for numbers in range(100):
		file.write('{}\n'.format(randint(1,500)))
	file.close()
def largest_smallest():
	file = open("100 random.txt","r")
	numbers =file.read().split('\n')
	del[numbers[-1]]
	for num in range(len(numbers)):
		numbers[num]=int(numbers[num])
	print("The largest number in the file is", max(numbers), "and the smallest is", min(numbers))	
	file.close()

#Store the file in the same directory as this program
#The file should have one integer on each line
def sumColumn(filename):
	"""This program reads a file that has exactly one integer on each line and returns the sum of these integers"""
	file = open(filename, 'r')
	numbers = file.read().split('\n')
	del (numbers[-1])
	for num in range(len(numbers)):
		numbers[num] = int(numbers[num])
	print("The sum of all the numbers in the list is", sum(numbers))	
	file.close()