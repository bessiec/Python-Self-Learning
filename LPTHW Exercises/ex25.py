#Learn Python the Hard Way Exercise 25: Even More Practice

def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return words

def sort_words(words):
	""" Sorts the words. """
	return sorted(words)

def print_first_word(words):
	""" Prints the first word after popping it off."""
	word = words.pop(0)
	print word

def print_last_word(words):
	""" Prints the last words after popping it off."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	""" Takes a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(Words)

def print_first_and_last(sentence):
	""" Prints the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words and then print the first and last one."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
