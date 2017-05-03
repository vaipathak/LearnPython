print "Exercise 19_5 - Vai's messing around with raw_input and functions."

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
print "Type in the number of cheese and the number of crackers you have:"
#we have to convert the "str" to an "int" using the "int()" function
cheese_and_crackers(int(raw_input() + 1), int(raw_input() + 2))
#Does not work - gives the error: TypeError: cannot concatenate 'str' and 'int' objects
#Might have to ask for raw input first or something.