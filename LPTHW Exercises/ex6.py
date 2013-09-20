#Learn Python the Hard Way Exercise 6: Strings and Text

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
#string inside string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

#string inside string
print "I said: %r" % x
#string inside string
print "I also said: '%s'." % y

#hilarious is false
hilarious = False

##defining variable
joke_evaluation = "Isn't that joke so funny!? %r"

# sending joke evalution and hilarious to to screen.  Semi-nested string?
print joke_evaluation % hilarious

#defining variable w
w ="This is the left of of..."

# defining variable e
e ="a string with the right side."

#sending w + e
print w + e