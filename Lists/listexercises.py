#Exercises from: http://interactivepython.org/courselib/static/thinkcspy/Lists/lists.html#exercises

a = [1, 2, 3]
b = a[:]
b[0] = 5
print b

mylist = [76, 92.3, "hello", True, 4, 76]
mylist.append("apple")
mylist.append(76)
mylist.insert(3, "cat")
mylist.insert(0, 99)

print(mylist.index("hello"))

print(mylist.count(76))

mylist.remove(76)

print(mylist.index(True))

remove_true = mylist.pop(4)

print mylist