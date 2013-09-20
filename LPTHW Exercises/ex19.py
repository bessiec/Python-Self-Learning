#Learn Python the Hard Way Exercise 19: Functions and Variables 

#defining a function cheese and crackers as cheese_count and boxes_of_crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print out cheese_count with this string
	print "You have %d cheeses!" % cheese_count
	# print otu boxes_of_crackers with this string
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for the party!"
	#make a linebreak with this statement
	print "Get a blanket.\n"

#giving the function as 20 and 30 
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# making variable names that equal numbers
print "OR, we can use the variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

#inserting the variable names to insert in new numbers for the fucntion
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#doing math in a variable and inserting answers into the function 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 +6)

#combining variables and math to insert solutions into function
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)