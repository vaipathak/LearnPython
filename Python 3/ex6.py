#LPTHW - Ex 6: Strings and Text
#Exercise creating a bunch of variables with complex strings.

#A string is usually a bit of text you want to display to someone
#or "export" out of the program you are writing.
#Python knows you want something to be a string when
#you put either " (double-quotes) or ' (single-quotes)
#around the text.

#Strings can contain any number of variables that are in
#your Python script. Remember that a variable is any line
#of code where you set a name = (equal) to a value.
#In the code for this exercise, types_of_people = 10
#creates a variable named types_of_people and sets it
# = (equal) to 10. You can put that in any string with
# {types_of_people}. You also see that I have to use a
#special type of string to "format"; it's called an "f-string"
#Python also has another kind of formatting using the
#.format() syntax used to apply a format to an already
#created string, such as in a loop.

types_of_people = 10
x = f"There are {types_of_people} types of people."
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))
w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
