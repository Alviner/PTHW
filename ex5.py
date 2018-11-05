# -*- coding: utf-8 -*-

my_name = "Zed A. Show"
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # ibs
my_eyes = "Blue"
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s" % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actualy that's not too heavy."
print "He's got %s eyes and %s heir." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (my_age, my_height, my_weight,
    my_age + my_height + my_weight)
