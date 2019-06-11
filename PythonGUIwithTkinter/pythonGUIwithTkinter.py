from tkinter import *
def goodbyeGUI():
	"""A GUI application with a button labeled “Goodbye.” When the button is clicked, the window closes"""
	root = Tk()
	def goodbye():
		root.destroy()
	goodbyeButton = Button(root,text = "Goodbye",command = goodbye)	
	goodbyeButton.pack()
	root.mainloop()

def counterGUI():
	"""a GUI application with a single button. Initially the button is labeled 0, but each time it is clicked, the value on the button increases by 1."""
	root = Tk()
	number = IntVar()
	def counter():
		global number
		number.set(number.get()+1)
	changing_button = Button(root, textvariable = number, command = counter)
	changing_button.pack()
	root.mainloop()	

def DNAsequenceGUI():
	root = Tk()
	root.geometry('400x200')
	def dna():
		dna = user_input.get()
		no_of_a = dna.count('A')
		a = Label(root, text = "Num As:"+str(no_of_a))
		a.pack(side = LEFT)
		no_of_t = dna.count('T')
		t = Label(root, text = "Num Ts:"+str(no_of_t))
		t.pack(side = LEFT)
		no_of_c = dna.count('C')
		c = Label(root, text = "Num Cs:"+str(no_of_c))
		c.pack(side = LEFT)
		no_of_g = dna.count('G')
		g = Label(root, text = "Num Gs:"+str(no_of_g))
		g.pack(side = LEFT)

	user_input = Entry(root)
	count = Button(root, text ='Count',command = dna)	
	user_input.pack()
	count.pack()
	root.mainloop()

def tempConvertGUI():
	"""4.	Write a GUI application that looks like the image below. When a value is entered in the text field 
	and the Convert button is clicked, the value should be converted from Fahrenheit to Celsius and displayed in the window
	"""
	root = Tk()
	def convert():
		f = user_input.get()
		c = (int(f)-32)/1.8
		temp_c = Label(root, text =str(c))
		temp_c.pack()
	text = Label(root, text="Temperature in Fahrenheit")
	user_input = Entry(root)
	convert = Button(root, text="Convert",command=convert)
	quit_button = Button(root,text="Quit",command = root.destroy)
	text.pack()
	user_input.pack()
	convert.pack()
	quit_button.pack()
	root.mainloop()
tempConvertGUI()