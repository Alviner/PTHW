# -*- coding: utf-8 -*-

def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def substruct(a, b):
    print "SUBSTRUCTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def devide(a, b):
    print "DEVIDING %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = substruct(78, 4)
weight = multiply(90, 2)
iq = devide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle"

what = add(age, substruct(height, multiply(weight, devide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
