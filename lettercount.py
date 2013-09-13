#Hackbright Academy Exercise 5: https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise05

from sys import argv

script, filename = argv

txt = open(filename)

f = txt.read()

txt.close()

f.lower()

alphabet = [0] * 26

for char in f:
	if 97 <= ord(char) <= 122:
		alphabet[ord(char)-97] += 1

for item in alphabet:
	print item