[10, 20, 30, 40]
["spam", "bungee", "swallow"]

["hello", 2.0, 5, [10,20]]

vocabulary = ["interation", "selection", "control"]
numbers = [17, 123]
empty = []
mixedlist = ["hello", 2.0, 5*2, [10,20]]

print(numbers)
print(mixedlist)
newlist = [numbers, vocabulary]
print(newlist)

alist = ["hello", 2.0, 5, [10, 20]]
print(len(alist))
print(len(['spam!', 1, ['Brie', 'Roquefort', 'Pol le Veq', [1, 2, 3]]]))

alist = [3, 67, "cat", 3.14, False]
print(len(alist))

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(len(alist))

#Accessing Elements
numbers = [17, 123, 87, 34, 66, 8398, 44]
print(numbers[2])
print(numbers[9-8])
print(numbers[-2])
print(numbers[len(numbers)-1])

alist = [3, 67, "cat", [56, 57, "dog", [ ], 3.14, False]]
print(alist[2].upper())
print(alist[2][0])

#List Slices 

a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

alist = [3, 7, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[4:])
print(alist[2:])
print(alist[:2])
print(alist[:3])

# Lists are Mutable

fruit = ["banana", "apple", "cherry"]
print(fruit)

#Item assignments

fruit[0] = "pear"
fruit[-1] = "orange"
print(fruit)

#Splice Operators

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] =  ['x','y']
print(alist)

#Removing elements by assigning empty list

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] =[]
print(alist)

#Insert elements into list by squeeing them into an empty splice at a desired location

alist = ['a', 'd', 'f']
alist[1:1] = ['b', 'c']
print(alist)
alist[4:4] = ['e']
print(alist)

#list deletion

a = ['one', 'two', 'three']
del a[1]
print(alist)

alist = ['a', 'b', 'c', 'd', 'e', 'f']
del alist[1:5]
print(alist)

#Objects and References

a = "banana"
b = "banana"

#We test whether two names refer to same object using the is operator in addition to unique identifer.
#is operater will return true if the two references are to the same object

print(a is b)

#True means that this refers to same object.  Python optimizes resources by making two names that point to the same string value refer to the same object.
#This is not the case with lists

a = [81, 82, 83]
b = a[:]
print a
print b

#a and b have the same value, but they do not refer to the same object
print(a is b)

print(a == b)

#Aliasing
#Since variables refer to objects, if we assign one variable to another, both variables refer to the same object.
a = [81, 82, 83]
b = a
print(a is b)

#Because the list has two different names, a and b, we can say that is is aliased.
#Changes made in one alias will affect the other.
#Because the variables are now alias, they have the same id in codelens after assignment statemment b=a.


#Repetition and References

origlist = [45, 75, 34, 55]
print(origlist*3)

#repetition operator creates copies of references

#Whe we allow a list to refer to a another list and use the reptition operator, we will create nested lists
newlist = [origlist] * 3

print(newlist)

origlist[1] = 99

print(newlist)

#newlist shows change in three places because there is only one origlist, so any changes will show up in all three references from the newlist

