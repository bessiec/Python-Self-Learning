#Learn Python the Hard Way Exercise 24: More Practice

print "Let's practice everything."

#using escapes 
print 'You\'d need to know \'bout escapes with \\ that do \n new lines and \t tabs.'

#poem with tabbing and line breaks 
poem = """

\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

#printing poem with ----- before and after
print "------------"
print poem
print "------------"

#defining five
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#creating secret formula function 
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

#defining starting point and variables with def function
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#print out each varaible
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#defines the start point 
start_point = start_point / 10

print "We can also do that this way:"
#print out variables using the secret formula definition
print "We'd have %d beans, %d jars, and %d creates." % (secret_formula(start_point))
