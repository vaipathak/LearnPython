print "Exercise 16: Reading and Writing Files"
#If you did the Study Drills from the last exercise you should have seen
# all sorts of commands (methods/functions) you can give to files. 
#Here's the list of commands I want you to remember:

#close -- Closes the file. Like File->Save.. in your editor.
#read -- Reads the contents of the file. You can assign the result to a variable.
#readline -- Reads just one line of a text file.
#truncate -- Empties the file. Watch out if you care about the file.
#write('stuff') -- Writes "stuff" to the file.

from sys import argv 
script, filename = argv
#uses argv to get a filename - in this case "test.txt" which we write in the command line.
print "We're going to erase %r." % filename
print "If you DON'T want that, hit CTRL-C (^C)."
print "If you DO want that, hit RETURN"
#How does it know to quit if "Ctrl-C is typed?"
raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
#opening a file with the 'w' opens it in "write-mode" so the next "truncate"
#line is redundant (done on purpose to show the two different options).
#If we just use "open(filename)" it opens the file in "read mode" only.
print "Truncating the file. Goodbye"
target.truncate()

print "Now I'm going to ask you for three lines."
#Entering 3 lines by the user:
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#Writes what the user input as "line1, line2, and line3 into the file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()
#Closes the file

#What modifiers to the file modes can I use?
#The most important one to know for now is the + modifier, so you can do 
#'w+', 'r+', and 'a+'. This will open the file in both read and write mode, 
#and depending on the character use position the file in different ways.