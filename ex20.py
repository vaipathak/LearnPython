print "Exercise 20: Functions and Files"
from sys import argv

script, input_file = argv
#we input our "input_file"

#Here we first define our functions.
#NOTE: What is "f" in the print_all and other functions?
#The "f" is a variable just like you had in other functions in Exercise 18, 
#except this time it's a file. 
#A file in Python is kind of like an old tape drive on a mainframe, 
#or maybe a DVD player. 
#It has a "read head," and you can "seek" this read head around the file to 
#positions, then work with it there. 
#Each time you do f.seek(0) you're moving to the start of the file. 
#Each time you do f.readline() you're reading a line from the file, 
#and moving the read head to right after the \n that ends that line. 
#This will be explained more as you go on.

#Reads the input file and prints the contents so f is the value given to "current_file"
def print_all(f):
	print f.read()

#Goes to the beginning of the file 	
def rewind(f):
	f.seek(0)

#	
def print_a_line(line_count, f):
	print line_count, f.readline()

#curret_file becomes the value of "input_file" - the file that we added as an 
#argument in argv. 	
current_file = open(input_file)

print "First let's print the whole file:\n"
#prints the entire contents of current file.
#Also, here is where current_file becomes "line_count" since the value of "current_file"
#gets transistioned into the "print_all" function with variable "line_count".
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines."

#Can I make this iterrative? 
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

#To use a short hand notation ("+=" where x = x+y is the same as x+=y), 
#we can do the following: 
#current_line = 1
#print_a_line(current_line, current_file)

#current_line += 1
#print_a_line(current_line, current_file)

#current_line += 1
#print_a_line(current_line, current_file)
