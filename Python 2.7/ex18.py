print "Exercise 18: Names, Variables, Code, Functions"
print """Big title, right? I am about to introduce you to the function! Dum dum dah! Every programmer will go on and on about functions and all the different ideas about how they work and what they do, but I will give you the simplest explanation you can use right now.

Functions do three things:

They name pieces of code the way variables name strings and numbers.
They take arguments the way your scripts take argv.
Using 1 and 2 they let you make your own "mini-scripts" or "tiny commands."
You can create a function by using the word def in Python. I'm going to have you make four different functions that work like your scripts, and I'll then show you how each one is related.
"""

#this one is like your scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
#Side Note: What does the * in *args do?
#That tells Python to take all the arguments to the function and then put them
#in args as a list. It's like argv that you've been using, but for functions. 
#It's not normally used too often unless specifically needed.
	
#ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#this one just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothin'."
	
print_two("Vai","Pathak")
print_two_again("Vai", "Pathak")
print_one("First!")
print_none()

#Let's break down the first function, "print_two", which is the most similar to 
#what you already know from making scripts:

#First we tell Python we want to make a function using "def" for "define".
#On the same line as def we give the function a name. 
#In this case we just called it "print_two" but it could also be "peanuts". 
#It doesn't matter, except that your function should have a short name that says
#what it does.
#Then we tell it we want *args (asterisk args) which is a lot like your 
#"argv" parameter but for functions. This has to go inside () parentheses to work.
#Then we end this line with a : colon, and start indenting.
#After the colon all the lines that are indented four spaces 
#will become attached to this name, print_two.
#Our first indented line is one that unpacks the arguments 
#the same as with your scripts.
#To demonstrate how it works we print these arguments out, just like we would 
#in a script.
#The problem with print_two is that it's not the easiest way to make a function.
#In Python we can skip the whole unpacking arguments and just use the names we want
#right inside (). That's what print_two_again does.

#After that you have an example of how you make a function that takes 
#one argument in print_one.

#Finally you have a function that has no arguments in print_none.

#Study Drill
#def check_list():
		