#Exercise One at Hackbright Academy.  https://github.com/chriszf/Hackbright-Curriculum/tree/master/Exercise01 
#Extra typing practice for myself and review. 
"""
I'm writing a program that will choose a random number between 1 to 100.  The computer
will choose a random number between 1 and 100, and ask the user to guess the number, giving them
a hint of it's too high or to low.  The logic of the program should go as such below

    greet player
    get player name
    choose random number between 1 and 100
    while True:
        get guess
        if guess is incorrect:
            give hint
        else:
            congratulate player

"""

import random

def main():
	player_name = raw_input("Name? \n")
	my_number = random.randint(1, 100)

	print "%s, I'm thinking of a number between 1 and 100.  Try to guess my number" % player_name

	guess = None

	while guess != my_number:

		raw_guess = raw_input("What is your guess?\n")
		guess = int(raw_guess)

		if guess > my_number:
			print "Your guess is too high."
		elif guess < my_number:
			print "Your guess is too low."
		if guess == my_number:
			print "You guessed correctly!  Congrats!"

if __name__ == "__main__":
	main()