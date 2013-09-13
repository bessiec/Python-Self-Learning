#Learn Python the Hard Way Exercise 15: Reading Files


# using argument variable to get feature from sys package
from sys import argv

#getting filename 
script, filename = argv

#open command 
txt = open(filename)

#printing what filename is and filename
print "Here's your file %r:" % filename
print txt.read()

#promoting to type in filename again 
print "Type the filename again:"
file_again = raw_input("> ")

#getting the file name form the raw imput
txt_again = open(file_again)

# printing out/re-opening txt file again
print txt_again.read()