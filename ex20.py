# -*- coding: utf-8 -*-

from sys import argv # import necessary modules

script, input_file = argv # parce input arguments

# define function to print file's content
def print_all(f):
    print f.read() # fet content of file object


# define function to return to the start of file
def rewind(f):
    f.seek(0) # return to start of file object


# define a function  for printing one line from file (also move file position to next line)
def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file) # open file (create file object)

print "First let's print a whole file:\n"

print_all(current_file) # print file's content

print "Now let's rewinf, kind pf like a tape."

rewind(current_file) # change file position to start

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file) # print one line

current_line += 1
print_a_line(current_line, current_file) # print next one line

current_line += 1
print_a_line(current_line, current_file)  # print also next one line

current_file.close() # close file object
