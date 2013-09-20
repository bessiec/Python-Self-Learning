#Hackbright Exercise 6 Redux/Review in funemployment grad school time
#https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise06


from sys import argv
script, filename = argv

f = open(filename).read().lower() #open and read the file, makes it into one string lowercase
f.close() #close the file
f_split = f.split() #split the string into a list

f_dict = {} #initialize a dictionary

for index in range(len(f_split)):
	#loop over range of length of list 
	word = f_split[index]
	f_split[index] = word.strip('.')
	#reassign the striped word back into f_split

for f in f_split:
	f_dict[word] = f_dict.get(word, 0) + 1 #fun with tuples to see if key exists, if it doesn't, return 0