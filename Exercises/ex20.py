#Learn Python the Hard Way Exercise 20: Functions and Files

#importing argument variable from system
from sys import argv

#the script will run the argv on the input_file
script, input_file = argv

#definining function print_all which prints the input file
def print_all(f):
	print f.read()

#defining a function that moves to start of input file
def rewind(f):
	f.seek(0)

#defines a function the gives line count and reads the line
def print_a_line(line_count, f):
	print line_count, f.readline()

#opens the input file
current_file = open(input_file)

#states to print a file and line break
print "First let's print the whole file:\n"

#calls print_all function on the opened input file
print_all(current_file)

#states that you are going to start rewind function
print "Now let's rewind, kind of like a tape"

#runs rewind function on current file (which seeks to go back 
# to beg of the file)
rewind(current_file)

print "Let's print three lines:"

# now redefines current_line varialbe as 1 and prints the current line added onto current_file
current_line = 1
print_a_line(current_line, current_file)

# redefines current_line variable + 1 and prints current line and current file
current_line = current_line + 1
print_a_line(current_line, current_file)

# redefines current_line variable + 1 and prints current line and current file
current_line = current_line + 1
print_a_line(current_line, current_file)

