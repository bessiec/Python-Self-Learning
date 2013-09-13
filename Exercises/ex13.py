#Learn Python the Hard Way Exercise 13: Parameters, Unpacking, Variables

#This is an import.  This is used to add features to script from the Python feature set.
#argv is the argument variable that holds the arguments you pass to your Python script when you run it.
#sys is a feature/module/library

from sys import argv

#This line "unpacks" argv so rather than holding all the arguemtns, it gets assigned to the variables so you can work with them.
script, first, second, third = argv

first = raw_input("Name something: \n")
second = raw_input("Name another thing: \n")
third = raw_input("Name another thing: \n")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
