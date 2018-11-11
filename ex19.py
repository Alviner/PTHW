# -*- coding: utf-8 -*-

# let's define function for printing amount our cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count # print cheese count
    print "You have %d boxes of crackers!" % boxes_of_crackers # print crackers count
    print "Man that's enough for a party!" # Go go go
    print "Get a blanked.\n" # last print and create empty line


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) # lets try use our new function

print "OR, we can use variables from our script:"
amount_of_cheese = 10 # define variable for amount of cheese
amount_of_crackers = 50 # define variable for amount of crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers) # use our variables in function

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) # use our function with math expressions

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # and lets combine math expressions with variables
