# -*- coding:  utf-8 -*-

from sys import argv

script, filename = argv # parse arguments

txt = open(filename) # open file and getting fileobject

print "Here's your file %r:" % filename # print filename

print txt.read() # get file content

print "Type the filename again:" # Let's continue
file_again = raw_input('--> ') # getting another filename

txt_again = open(file_again) # open file and getting fileobject

print txt_again.read() # get content another filename

txt.close()
txt_again.close()
