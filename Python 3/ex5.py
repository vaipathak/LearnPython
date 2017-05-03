# LPTHW - Ex.5 More Variables and Printing - format strings

#Note: Anything between "" are called strings.
#We can embed variables within strings by using the
#{} brackets!

name = 'Vai Pathak'
age = 34
height = 73 #inches
weight = 186 #lbs
eyes = 'Light Brown'
teeth = 'White'
hair = "Black"

print(f"Let's talk about {name}.")
print(f"He's {height} inches all.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight

print(f"If I add {age}, {height}, and {weight}, I get {total}.")

height_feet = round(73/12) #feet
weight_kg = round(186/2.2) #kgs

print(f"The height is {height_feet} in feet and weight is {weight_kg} in kilograms.")
