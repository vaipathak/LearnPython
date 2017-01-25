print "This is exercise 6 - Strings and Text"
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x #Will print "There are 10 types of people"
print y #Will print "Those who know binary and those who do not"

print "I said: %r." % x #will print "I said" and a repeat of x
print "I also said: '%s'." % y #will print " I also said" and repeat of y

hilarious = False #gives hilarious the value of "False"
joke_evaluation = "Isn't that joke so funny?! %r"
#Gives "joke_evaluation" the value of "Isn't that joke funny?!"

print joke_evaluation % hilarious #hilarious is the format string for %r

w = "This is the left side of..."
e = "a string with a right side."

print w + e

#Faq: What is the difference between %r and %s?
#Use the %r for debugging, since it displays the "raw" data 
#of the variable, but the others are used for displaying to users.