#LPTHW - Exercise 4 Variables and Names

#Variable for number of cars
cars = 100
#Variable for number of spaces in a car
space_in_a_car = 4.0
#Variable for the number of drivers
drivers = 30
#Variable for number of passengers
passengers = 90
#Calculating cars not driven
cars_not_driven = cars - drivers
#Caclulating cars driven
cars_driven = drivers
#Calculating the carpool capacity by multiplying cars driven by spaces available
carpool_capacity=cars_driven * space_in_a_car
#Calculating the average number of passengers per car
average_passengers_per_car=passengers / cars_driven


#How many cars available?
print("There are", cars, "cars available.")
#How many drivers available?
print("There are only", drivers, "drivers available.")
#How many empty cars?
print("There will be", cars_not_driven, "empty cars today.")
#How many people can we transport?
print("We can transport", carpool_capacity, "people today.")
#How many passengers needed to carpool?
print("We have", passengers, "to carpool today.")
#How many passengers per car?
print("We need to put about", average_passengers_per_car,
      "in each car.")

#Getting an error that says ""'Variable' name is not defined
#just means you forgot to define the variable either by omitting it
#or by a typo during the variable defining line 
