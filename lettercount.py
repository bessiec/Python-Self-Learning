#Hackbright Academy Exercise 5: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise05
#Re-doing exercise to review/guilt in funemplyoment


from sys import argv #importing argument variable 
script, filename = argv #adding python feature sets 


txt = open(filename) #defining variable txt as contents of open file
f = txt.read() #reading the text fail

txt.close() # closing the file
f.lower() #lower all the characters to avoid duplicate counts 

alphabet = [0] * 26 #defining number items in alphabet 

for char in f:
	if 97 <= ord(char) <= 122: # defining ASCII value range to add every place
		alphabet[ord(char)-97] += 1 # adding each place by 1 to arrive at proper ASCII value 

for item in alphabet: #iterate through and print every item
	print item
