#Learn py the hard way ex 5

my_name = 'V. S. Pathak'
my_age = 33 # not a lie
my_height = 73 #inches
my_weight = 186 #lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Lets' talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d - I get %d" %(my_age, my_height, my_weight, my_age + my_height + my_weight)

#%s and %d are placeholders for string values. ie %s is used as a place holder for 
#string values you want to inject into a formatted string. 
#%d is used as a placeholder for numeric or decimal values. 
#ie name = 'marcog'
#   number = 42
#   print '%s %d' % (name, number)