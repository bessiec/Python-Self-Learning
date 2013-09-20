#Learn Python the Hard Way Exercise 14: Prompting and Passing
 
from sys import argv

script, user_name = argv
Link = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(Link)

print "Where do you live %s" % user_name
lives = raw_input(Link)

print "What kind of computer do you have?"
computer = raw_input(Link)

print "What kind of eggs do you like?"
eggs = raw_input(Link)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure what that is.
And you have a %r computer. Nice.
You also like %r eggs.  Cool
""" % (likes, lives, computer, eggs)