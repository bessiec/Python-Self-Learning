#List Methods

#adds everything to a list
mylist = []
mylist.append(5)
mylist.append(27)
mylist.append(3)
mylist.append(12)
print(mylist)

#inserts 13 into position 1
mylist.insert(1, 12)
print(mylist)
#returns number of occurances per item
print(mylist.count(12))	
print(mylist.count(5))
print(mylist.count(4))

#returns place of item in the list 
print(mylist.index(3))
print(mylist.index(12))
print(mylist.index(27))
print(mylist.count(5))

#reverse the list 
mylist.reverse()
print(mylist)

#modifies a list to be sorted
#It's important to note that append, sort, and serve all return None.  
#This means reassigning mylist to the result of sorting my list will result in losing the entire list.
mylist.sort()
print(mylist)

#removing first occurance of an item
mylist.remove(5)
print(mylist)

#removes and returns last time at position
lastitem = mylist.pop()
print(lastitem)
print(mylist)

#Append versus Concatenate

#append only modifies original list (same id)
#you cannot concatenate a list with an integer
origlist = [45, 32, 88]
origlist.append("cat")

print origlist

#changes the id
origlist = origlist + ["cat"]

print origlist

testlist = [31, 35, 40]
testlist.append(52)

print testlist

#Lists and for loops

fruits = ["apple", "orange", "banana", "cherry"]

for afruit in fruits: 
	print(afruit)

#Use indices to access the items in an iterative fashion
for position in range(len(fruits)):
	print(fruits[position])

#Range function returns a sequence of numbers
#This prints all the multiples of 3 between 0 and 19
for number in range(20):
	if number % 3 == 0:
		print(number)

#Since lists are mutable, it is often desirable to traverse a list, modifying each of its
#elements as you go.  This code squares all numbers 1 to 5, using iteration by position

numbers = [1, 2, 3, 4, 5]
print(numbers)

for i in range(len(numbers)):
	numbers[i] = numbers[i]**2

print(numbers)

number2 = [2, 4, 5, 7, 6]
for i in range(len(number2)):
	number2[i] = number2[i]**2
print(number2)

#add every item in alist + 5 to blist
alist = [4, 2, 8, 6, 5]
blist = []
for item in alist:
	blist.append(item+5)
print(blist)

#Using List as Parameters

#Passing a list as an argument actually passes a reference to the list, not a copy of the list.

#Functions which takes lists as arguments and change them during execution are called modifers and they changes they make are called side effects.
def doubleStuff(alist):
	""" Overwrite each element in aList with double its value """
	for position in range(len(alist)):
		alist[position] = 2 * alist[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)
