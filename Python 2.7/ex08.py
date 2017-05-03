print "Exercise 8  Printing, printing"

formatter = "%r %r %r %r" #format strings for the value "formatter"
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", #This line will print out in double quotes 
	"So I said goodnight."
)

#Faqs
#Should I use %s or %r for formatting?
#You should use %s and only use %r for getting debugging information 
#about something. The %r will give you the "raw programmer's" version
#of variable, also known as the "representation."
#
#I tried putting Chinese (or some other non-ASCII characters) into these strings, but %r prints out weird symbols.
#Use %s to print that instead and it'll work.

#Not this formatting doesn't work in Python 3.