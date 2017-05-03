print "Exercise 9 - Printing, Printing, Printing"

days = "Mon Tue Wed Thu Fri Sat Sun"
# prints all days on one line
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#My guess is that it prints the months, each on a new line -> I was right

print "Here are the days: ", days
#interesting there's no string formmatter here
#NOTE - comma is needed after!
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much a we like.
Even 4 lines if we want, or 5, or 6.
"""
#That's cool to know.

#Faq
#Why do the \n newlines not work when I use %r?
#That's how %r formatting works; it prints it the way you wrote it 
#(or close to it). It's the "raw" format for debugging.