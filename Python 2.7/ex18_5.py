print "Exercise 18_5 - Vai's messing around with raw_input and functions."
print "Type in two arguments - if this works, whatever you typed will be repeated."
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
print_two_again(raw_input(),raw_input())
	
