#Hackbright Exercise 6 Redux/Review in funemployment grad school time
#https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise06

from sys import argv
import string
import re
script, filename = argv

text = open(filename).read().lower() #open and read the file, makes it into one string lowercase

text = re.sub("["+string.punctuation+"]", '', text)


word_count = {}

for word in text:
	word_count[word] = word_count.get(word, 0) +1 

for word, num in word_count.iteritems():
	print "The word %s occurs %d times." % (word, num) 


word_count_ordered = sorted(word_count.iteritems(), key = lambda word: (word[1], word[0]), reverse = False)

for word, num in word_count_ordered:
	print "The word %s occurs %d times." % (word, num) 