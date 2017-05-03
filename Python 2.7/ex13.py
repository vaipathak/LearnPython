print "Exercise 13: Paremeters, Unpacking, Variables."
#In this exercise we will cover one more input method 
#you can use to pass variables to a script 
#(script being another name for your .py files). 
#You know how you type python ex13.py to run the ex13.py file? 
#Well the ex13.py part of the command is called an "argument." 
#What we'll do now is write a script that also accepts arguments.

from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

#Pay attention! You have been running python scripts without command line 
#arguments. If you type only python ex13.py you are doing it wrong! 
#Pay close attention to how I run it. This applies any time you see "argv" 
#being used.

#On line 9 we have what's called an "import." This is how you add 
#features to your script from the Python feature set. Rather than
#give you all the features at once, Python asks you to say what you 
#plan to use. This keeps your programs small, but it also acts as 
#documentation for other programmers who read your code later.

#The argv is the "argument variable," a very standard name in programming, 
#that you will find used in many other languages. This variable holds 
#the arguments you pass to your Python script when you run it. 
#In the exercises you will get to play with this more and see what happens.

#Line 11 "unpacks" argv so that, rather than holding all the arguments, 
#it gets assigned to four variables you can work with: script, first, second, 
#and third. This may look strange, but "unpack" is probably the best word to 
#describe what it does. It just says, "Take whatever is in argv, unpack it, 
#and assign it to all of these variables on the left in order."

#Run the program like this (and you must pass three command line arguments):

#$ python ex13.py first 2nd 3rd
#The script is called: ex13.py
#Your first variable is: first
#Your second variable is: 2nd
#Your third variable is: 3rd

#You can actually replace first, 2nd, and 3rd with any three things you want.

#If you do not run it correctly, then you will get an error like this:

#$ python ex13.py first 2nd
#Traceback (most recent call last):
 # File "ex13.py", line 3, in <module>
  #  script, first, second, third = argv
#ValueError: need more than 3 values to unpack
#This happens when you do not put enough arguments on the command when you run it
# (in this case just first 2nd). Notice when I run it I give it first 2nd, 
#which caused it to give an error about "need more than 3 values to unpack" 
#telling you that you didn't give it enough parameters.

#Study Drill - Combine argv and raw_input
#Ans: 
#from sys import argv

#script, first, second, third = argv
#fourth = raw_input("What is your fourth variable? ")

#print "All together, your script is called %r, your first variable is %r, 
#your second is %r, your third is %r, and your fourth is %r" % (script, first, 
#second, third, fourth)
