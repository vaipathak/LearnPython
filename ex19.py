print "Exercise 19: Functions and Variables"
print """Functions may have been a mind-blowing amount of information, 
but do not worry. Just keep doing these exercises and going through your checklist
from the last exercise and you will eventually get it.

There is one tiny point that you might not have realized, which we'll reinforce 
right now. The variables in your function are not connected to the variables
in your script. Here's an exercise to get you thinking about this:
"""

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
print "We can just give the fnction numbers directly:"
cheese_and_crackers(20,30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two - variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

