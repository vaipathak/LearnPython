print "Exercise 7: More Printing"
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' #note the quotes to designate a
                                             #string and not a value
print "And everywhere that Mary went."
print "." * 10 # What'd that do? -> it printed 10 dots 

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. try removing it and see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

#without commma
print end1 + end2 + end3 + end4 + end5 + end6
print end7 + end8 + end9 + end10 + end11 + end12

#Without the comma, it prints "Cheese burger" on two different lines
#With a comma, there's a space "Cheese burger" and on the same line