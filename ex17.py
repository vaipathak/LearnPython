print "Exercise 17: More files"
print """In this exerise we'll write a Python script to copy one file to another. 
It'll be very short but will give you ideas about other things you can do with files.
"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

#We can do these two on one line, how? 
# My ans is wrong. Found on internet: open(to_file, 'w').write(open(from_file).read())
in_file = open(from_file)
#gives infile the value from "from_file"
indata = in_file.read()
#indata is given the value from in_file

print "The input file is %d bytes long" % len(indata)
#gives the length of the "from file"
print "Does the output file exist? %r?" % exists(to_file)
#checks to see if the output file exits via the "exists()" function.
print "Ready, hit the RETURN to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
#opens a file to write and gives that value to "out_file" aka truncates "to_file"
out_file.write(indata)
#writes indata to out_file
print "Alright, all done."

out_file.close()
in_file.close()