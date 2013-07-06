#Creating a dictionary

eng2sp = {}
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tres'

eng2sp = {'three': 'tres', 'one': 'uno', 'two': 'dos'}
print(eng2sp)

mydict = {"cat":12, "dog":6, "elephant":23}
print(mydict["dog"])

#Dictionary Items

#Del a key-value pair from dictionary 

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears':217}

print inventory

del inventory['pears']

print inventory

#Dictionaries are mutable, meaning the dictionary can be modified by referencing an assoication on left side of the assignment statement.

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears':217}

inventory['pears'] = 0

print inventory

#New shipmen of 200 bananas

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears':217}
inventory['bananas'] = inventory['bananas'] + 200

numItems = len(inventory)

print numItems

#question

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears':217}

for akey in inventory.keys():  #the order in which we get keys is not defined 
	print("Got key", akey, "which maps to value", inventory[akey])

ks = list(inventory.keys())
print(ks)

for k in inventory:
	print("Got key", k)
