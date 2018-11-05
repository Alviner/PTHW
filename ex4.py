# -*- coding: utf-8 -*-

cars = 100  # Let's define a number of cars

space_in_a_car = 4.0 # It it a space in one car
drivers = 30 # Oh we need some drivers for our cars
passengers = 90 # And some passengers
cars_not_driven = cars - drivers # Cars without
cars_driven = drivers # Used cars
carpool_capacity = cars_driven * space_in_a_car # Space that we can filled
avarage_passengers_per_car = passengers / cars_driven # Avarage passengers in used cars


print "There are", cars, "cars availabe."
print "There are only", drivers, "drivers availabe."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", avarage_passengers_per_car, "in each car."
