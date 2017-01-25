#sets the variable "car" to 100
cars=100
#sets how many spaces there are in a car (note floating number)
space_in_a_car = 4.0
#Number of drivers is 30
drivers = 30
#number of passengers is 90
passengers = 90
#math to find the number of cars ot driven
cars_not_driven = cars - drivers
#cars driven
cars_driven = drivers
#calculating the carpool capacity
carpool_capacity = cars_driven * space_in_a_car
#calculating an average
ave_pass_per_car = passengers / cars_driven

print "There are", cars, "cars available"
print "There are only", drivers, "drivers available"
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put about", ave_pass_per_car, "in each car"