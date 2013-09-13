#Learn Python the Hard Way Exercise 18: Variables, Codes, Functions

#this one is like the scripts with argv.  
# it defines a function as the print of arg1: "" and arg2""
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#ok so that *args was actually pointless, we can do this instead
#this one simplies the function above without the *args and line four 
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument, which is arg1:""
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments and will just pint the below
def print_none():
	print "I got nothin'."

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
	