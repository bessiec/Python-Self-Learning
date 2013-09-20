#Learn Python the Hard Way Exercise 33: While Loops

i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i 
	numbers.append(i)

	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i

j = 3
numbers2 = []
while j < 10:
	print "At the top j is %d" % j
	numbers2.append(j)

	j = j + 1
	print "Numbers2 now: ", numbers2
	print "AT the bottom j is %d" % j

x = 0
numbers3 = []
for x in range(0,6):
	print "At the top is x is % d" % i
	numbers3.append(x)

	x = x + 1
	print "Numbers3 now: ", numbers3
	print "At the bottom x is %d" % x


