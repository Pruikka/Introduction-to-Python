#This here is a comment line!
## This here also is
print("Action!") # and a comment

variable_1 = "Stringline!"
variable_2 = "Llamas?"
print(variable_1)

value = input("Write something and press enter: ")
print(value)

addition = "string-type content"
print("Our variable has a value which is ",addition,". Isn't that nice?",sep="")

number1 = 1000
number2 = 24
result = (number1 + number2 + 15)**2
print("The final results of the calculation was:",result)

variable_1 = 10.6411
variable_2 = "Stringline!"

variable_1 = int(variable_1)
variable_2 *= 2

print("Integer conversion cannot do roundings:",variable_1)
print("Multiplying strings also causes trouble:",variable_2)

print("""This here is divided to several lines:
I am still in the same print-command.
\t\tName:\tPeter
\t\tJob:\tBabysitter""")

#Exercise 2.5: Calculator, taking an input
print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))
print("The result is:",num1 + num2)

#Exercise 2.6: String slices
str = "desserts"
a = str[:4]
b = str[4:]
c = str[::-1]

print("The first 4 characters were:",a)
print("The last 4 characters were:",b)
print("The string backwards was:",c)

color = "black"
if color == "black":
    print("A bit gloomy here.")

name = "Carl"
if name == "Matt":
    print("Hi Matt!")
else:
    print("Oh you are somebody else.")

selection = "tricycle"

if selection == "money":
    print("You selected the money!")
elif selection == "tricycle":
    print("You selected the tricycle!")
else:
    print("Nothing.")

textline = "applejuice"

if textline == "applejuice":
    print("My favorite!")

#Exercise 3.1: The basic if-structure
number = int(input("Give a number: "))
if (number % 2 == 0):
	print("The given number was even.")

#Exercise 3.2: Structures within structures
name = input("Give name: ")
if name == "John":
	password = input("Give password: ")
	if password == "ABC123":
		print("Both inputs are correct!")
	else:
		print("The password is incorrect.")
else:
	print("The given name is wrong.")

#Exercise 3.3: Complete if-structure
number = int(input("Select a number (1-3): "))
if number == 1:
	print("You selected one.")
elif number == 2:
	print("You selected two.")
else:
	print("You selected three.")

#Exercise 3.4: Using several parameters
num1 = int(input("Give a number: "))
num2 = int(input("Give another number: "))

if (num1 % 2 == 0) and (num2 % 2 == 0):
	print("Both numbers are even.")
elif (num1 % 2 != 0) and (num2 % 2 != 0):
	print("Both numbers are odd.")
else:
	print("One of the numbers is even.")

#Exercise 3.5: Calculator, different types of calculations
print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

print("(1) +\n(2) -\n(3) *\n(4) /")
selection = int(input("Please select something (1-4): "))

if selection == 1:
    print("The result is:",num1 + num2)
elif selection == 2:
    print("The result is:",num1 - num2)
elif selection == 3:
    print("The result is:",num1 * num2)
elif selection == 4:
    print("The result is:",num1 / num2)
else:
    print("Selection was not correct.")

#Exercise 4.1: While-structure
count = 0
while count < 5:
	print("This is lap",count)
	count += 1

#Exercise 4.2: While-structure with ending criteria
while True:
	userIn = input("Write something: ")
	if userIn == "quit":
		print("Bye bye!")
		break
	print(userIn)

#Exercise 4.3: For in range
number = int(input("Give a number: "))
sum = 0

for i in range(0, number):
	sum += i

print("The sum was:",sum)

#Exercise 4.4 Calculator: Several options, changing the number
print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

while True:
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5)Change numbers\n(6)Quit")
	print("Current numbers:",num1,num2)
	selection = int(input("Please select something (1-6): "))

	if selection == 1:
		print("The result is:",num1 + num2)
	elif selection == 2:
		print("The result is:",num1 - num2)
	elif selection == 3:
		print("The result is:",num1 * num2)
	elif selection == 4:
		print("The result is:",num1 / num2)
	elif selection == 5:
		num1 = int(input("Give the first number: "))
		num2 = int(input("Give the second number: "))
	elif selection == 6:
		print("Thank you!")
		break
	else:
		print("Selection was not correct.")

#Exercise 5.1: Reading a file
readfile = open("facts.txt", "r")
content = readfile.read()
print("Following was read from the file:",content)
readfile.close()

#Exercise 5.2: Writing to a file
filename = input("Give a file name: ")
content = input("Write something: ")

myfile = open(filename, "w")
myfile.write(content)
myfile.close()

print("Wrote",content,"to the file",filename)

#Exercise 5.3: Filtering the file contents
readfile = open("strings.txt")
lines = readfile.readlines()
for line in lines:
	line = line[:-1]
	if line.isalnum():
		print(line + " was ok.")
	else:
		print(line + " was invalid.")
readfile.close()

#Exercise 5.4 Notebook: Read and write to the notebook
while True:
    print("""(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit""")
    selection = int(input("Please select one: "))

    if selection == 1:
        notebook = open("notebook.txt")
        notes = notebook.read()
        print(notes)
        notebook.close()
    elif selection == 2:
        newnote = input("Write a new note: ")
        notebook = open("notebook.txt", "a")
        notebook.write(newnote)
        notebook.close()
    elif selection == 3:
        notebook = open("notebook.txt", "w")
        notebook.close()
        print("Notes deleted.")
    elif selection == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")

#Exercise 6.1: Basic subfunction
def hello():
	print("Hello there!")
	
def main():
	print("Lets call the subfunction:")
	hello()
	print("Quitting.")

if __name__ == "__main__":
	main()

#Exercise 6.2: Using parameters
def poweroftwo(num):
    return 2**num

def main():
    number = int(input("Give a number: "))
    print("The result is", poweroftwo(number))

if __name__ == "__main__":
    main()

#Exercise 6.3: Default parameters
def tester(givenstring = "Too short"):
    if len(givenstring) < 10:
        print("Too short")
    else:
        print(givenstring)
		
def main():
    while True:
        word = input("Write something (quit ends): ")
        if word == "quit":
            break
        tester(word)

if __name__ == "__main__":
	main()

#Exercise 6.4: Return value
def tester(givenstring = "Too short"):
    if len(givenstring) < 10:
        print("Too short")
        return False
    if "X" in givenstring and len(givenstring) > 10:
        print(givenstring)
        return True
    else:
        print(givenstring)
        return False
		
def main():
    while True:
        word = input("Write something (quit ends): ")
        if word == "quit":
            break
        flag = tester(word)
        if flag:
            print("X spotted!")
if __name__ == "__main__":
	main()

#Exercise 7.1: The random module, coin flipping
import random

num = random.randint(0,1)
if num == 0:
	print("Tails!")
else:
	print("Heads!")

#Exercise 7.2: Nuke-foot-cockroach
import random

rounds = 0
wins = 0
ties = 0

while True:
    player = input("Foot, Nuke or Cockroach? (Quit ends): ")
    computer = random.randint(1,3)
    if player == "Foot":
        print("You chose: Foot")
    elif player == "Nuke":
        print("You chose: Nuke")
    elif player == "Cockroach":
        print("You chose: Cockroach")
    elif player == "Quit":
        print("You played",rounds,"rounds, and won",wins,"rounds, playing tie in",ties,"rounds.")
        break
    else:
        print("Incorrect selection.")
        continue

    if computer == 1:
        print("Computer chose: Foot")
    elif computer == 2:
        print("Computer chose: Nuke")
    else:
        print("Computer chose: Cockroach")
	
    if player == "Foot" and computer == 3:
        print("You WIN!")
        wins += 1
    elif player == "Nuke" and computer == 1:
        print("You WIN!")
        wins += 1
    elif player == "Cockroach" and computer == 2:
        print("You WIN!")
        wins += 1
    elif player == "Nuke" and computer == 2:
        print("Both LOSE!")
    elif player == "Foot" and computer == 1:
        print("It is a tie!")
        ties += 1
    elif player == "Cockroach" and computer == 3:
        print("It is a tie!")
        ties += 1
    else:
        print("You LOSE!")
	
    rounds +=1

#Exercise 7.3: Creating own module
def printme(string):
    print("I got:",string)
    print("The parameter was",len(string),"characters long.")

#Exercise 7.4: Your own module with several parameters
def hasDigit(string):
    for i in string:
    if i.isdigit():
        return True
    return False

def hasAlpha(string):
    for i in string:
        if i.isalpha():
            return True
    return False

def testme(password):
    if len(password) >= 6 and hasAlpha(password) and hasDigit(password):
        return True
    else:
        return False

#Exercise 7.5: Calculator - math-library
import math

print("Calculator")
num1 = int(input("Give the first number: "))
num2 = int(input("Give the second number: "))

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
    print("Current numbers:",num1,num2)
    selection = int(input("Please select something (1-6): "))

    if selection == 1:
        print("The result is:",num1 + num2)
    elif selection == 2:
        print("The result is:",num1 - num2)
    elif selection == 3:
        print("The result is:",num1 * num2)
    elif selection == 4:
        print("The result is:",num1 / num2)
    elif selection == 5:
        print("The result is:",math.sin(num1 / num2))
    elif selection == 6:
        print("The result is:",math.cos(num1 / num2))
    elif selection == 7:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
    elif selection == 8:
        print("Thank you!")
        break
    else:
        print("Selection was not correct.")

#Exercise 7.6: Notebook - Adding dates to the system
import time

while True:
    print("""(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit""")
    selection = int(input("Please select one: "))

    if selection == 1:
        notebook = open("notebook.txt")
        notes = notebook.read()
        print(notes)
        notebook.close()
    elif selection == 2:
        newnote = input("Write a new note: ")
        time = time.strftime("%X %x")
        notebook = open("notebook.txt", "a")
        notebook.write(newnote + ":::"+time)
        notebook.close()
    elif selection == 3:
        notebook = open("notebook.txt", "w")
        notebook.close()
        print("Notes deleted.")
    elif selection == 4:
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection")

#Exercise 8.1: Basic exception handler
number = input("Give a number: ")
try:
    number = int(number)
    print("The input was suitable!")

except Exception:
    print("The input was malformed.")

#Exercise 8.2: Catching several errors at once
filename = input("Give the file name: ")
try:
	readfile = open(filename)
	number = int(readfile.read())
	result = 1000.0 / number
	
except IOError:
	print("There seems to be no file with that name.")
	
except (TypeError, ValueError):
	print("The file contents were unsuitable.")
	
else:
	print("The result was",result)

#Exercise 8.3: Calculator - Checking input validity
import math

def inputNumber():
	while True:
		try:
			num = int(input("Give a number: "))
			return num
		except Exception:
			print("This input is invalid.")

def main():
	print("Calculator")
	num1 = inputNumber()
	num2 = inputNumber()

	while True:
		print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
		print("Current numbers:",num1,num2)
		selection = int(input("Please select something (1-6): "))

		if selection == 1:
			print("The result is:",num1 + num2)
		elif selection == 2:
			print("The result is:",num1 - num2)
		elif selection == 3:
			print("The result is:",num1 * num2)
		elif selection == 4:
			print("The result is:",num1 / num2)
		elif selection == 5:
			print("The result is:",math.sin(num1 / num2))
		elif selection == 6:
			print("The result is:",math.cos(num1 / num2))
		elif selection == 7:
			num1 = int(input("Give the first number: "))
			num2 = int(input("Give the second number: "))
		elif selection == 8:
			print("Thank you!")
			break
		else:
			print("Selection was not correct.")

if __name__ == "__main__":
	main()

#Exercise 8.4: Notebook - Changing the written file
import time

nowopen = "notebook.txt"
try:
	notebook = open(nowopen)
except IOError:
	notebook = open(nowopen, "w")
	print("No default notebook was found, Created one.")

notebook.close()

while True:
	print("")
	print("Now using file " + nowopen)
	print("""(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit""")
	print("")
	selection = int(input("Please select one: "))

	if selection == 1:
		notebook = open(nowopen)
		notes = notebook.read()
		print(notes)
		notebook.close()
	elif selection == 2:
		notebook = open(nowopen, "a")
		newnote = input("Write a new note: ")
		now = time.strftime("%X %x")
		notebook.write(newnote + ":::" + now + "\n")
		notebook.close()
	elif selection == 3:
		notebook = open(nowopen, "w")
		notebook.close()
		print("Notes deleted.")
	elif selection == 4:
		nowopen = input("Give the name of the new file: ")
		try:
			notebook = open(nowopen)
			notebook.close()
		except IOError:
			notebook = open(nowopen, "w")
			print("No notebook with that name detected, created one.")
			notebook.close()
	elif selection == 5:
		print("Notebook shutting down, thank you.")
		break
	else:
		print("Incorrect selection")

#Exercise 9.1: Creating a list
mylist = ["Blue", "Red", "Yellow", "Green"]
print("The first item in the list is: " + mylist[0])
print("The entire list printed one item a time:")
for i in mylist:
	print(i)

#Exercise 9.2: Using the list
shoppinglist = []

while True:
	selection = int(input("""Would you like to
(1)Add or
(2)Remove items or
(3)Quit?: """))

	if selection == 1:
		addtolist = input("What will be added?: ")
		shoppinglist.append(addtolist)
	elif selection == 2:
		print("There are " + str(len(shoppinglist)) + " items in the list.")
		remove = int(input("Which item is deleted?: "))
		if remove >= len(shoppinglist):
			print("Incorrect selection.")
		else:
			shoppinglist.pop(remove)
	elif selection == 3:
		print("The following items remain in the list:")
		for i in shoppinglist:
			print(i)
		break
	else:
		print("Incorrect selection.")

#Exercise 9.3: More list methods
filename = open("words.txt")
content = filename.readlines()

wordlist = []

for i in content:
	wordlist.append(i)

wordlist.sort()

print("Words in an alphabetical order:")
for i in wordlist:
	print(i)

filename.close()

#Exercise 9.4: Notebook - Using list with the notebook, pickle
# -*- coding: cp1252 -*-

import time
import pickle

try:
	filename = open("notebook.dat", "rb")
	notebook = pickle.load(filename)
except IOError:
	filename = open("notebook.dat", "wb")
	print("No default notebook was found, created one.")
	notebook = []

while True:
	print("""(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit""")
	print("")

	selection = int(input("Please select one: "))
	
	if selection == 1:
		for i in notebook:
			print(i)
	elif selection == 2:
		newnote = input("Write a new note: ")
		now = time.strftime("%X %x")
		addnote = newnote + ":::" + now
		notebook.append(addnote)
	elif selection == 3:
		change = int(input("The list has " + str(len(notebook)) + " notes.\nWhich of them will be changed?: "))
		print(notebook[change-1])
		notebook.pop(change-1)
		newnote = input("Give the new note: ")
		now = time.strftime("%X %x")
		addnote = newnote + ":::" + now
		notebook.insert(change-1, addnote)
	elif selection == 4:
		delete = int(input("The list has " + str(len(notebook)) + " notes.\nWhich of them will be deleted?: "))
		print("Deleted note " + notebook[delete-1])
		notebook.pop(delete-1)
	elif selection == 5:
		pickle.dump(notebook, filename)
		print("Notebook shutting down, thank you.")
		break
        
#Exercise 10.1: Creating a class and an object
# -*- coding: cp1252 -*-

class Player:
	teamcolor = ""
	points = 0

def main():
	player1 = Player()
	player1.teamcolor = "Blue"
	player1.points = 300
	
	print("The",player1.teamcolor,"contender has",player1.points,"points!")
	
if __name__ == "__main__":
	main()

#Exercise 10.2: Creating a method
# -*- coding: cp1252 -*-

class Player:
	teamcolor = ""
	__points = 0
	
	def tellscore(self):
		print("I am" + self.teamcolor + ", we have",self.__points," points!")
	
	def goal(self):
		self.__points += 1

def main():
	player1 = Player()
	player1.teamcolor = "Blue"
	player1.goal()
	player1.tellscore()
	
if __name__ == "__main__":
	main()

#Exercise 10.3: Initializing a class
# -*- coding: cp1252 -*-

class Player:
	"""Player-class: stores data on team colors and points."""
	
	teamcolor = ""
	__points = 0
	
	def tellscore(self):
		print("I am" + self.teamcolor + ", we have",self.__points," points!")
	
	def goal(self):
		self.__points += 1

def main():
	player1 = Player()
	player1.teamcolor = input("What color do I get?: ")
	
	player2 = Player()
	player2.teamcolor = input("What color do I get?: ")
	
	
	player1.goal()
	player1.goal()
	player2.goal()
	
	player1.tellscore()
	player2.tellscore()
	
if __name__ == "__main__":
	main()

#Exercise 10.4: Inheritance
# -*- coding: cp1252 -*-

class Customer:
    name = "John Johnsson"
    total = 1000
    paymenttype = "Masterexpress"
    number = "1234-5678-9012345"

    def printout(self):
        print("Name: ", self.name)
        print("Total: ", self.total)
        print("Payment type: ", self.paymenttype)
        print("Card/Bill number: ", self.number)


### Teacher: Put your code here. Me: Ok, just a sec... :) ###
class ManageCustomer(Customer):
	def addbill(self):
		self.total += 50
	
	def payment(self):
		self.total -= 100

def main():
    person = ManageCustomer()
    person.name = "Homer Griffin"
    person.addbill()
    person.payment()
    person.payment()
    person.printout()
    
if __name__ == "__main__":
    main()