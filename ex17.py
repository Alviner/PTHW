# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do there on one line, how? --> in_data = open(from_file).read()
in_file = open(from_file)
in_data = in_file.read()

print "The input file if %d bytes long" % len(in_data)
print "Ready, hit RETURN to continue, CTRL-C (^C) to abort."
raw_input()
out_file = open(to_file, 'w')
out_file.write(in_data)

print "Alright, all done."
out_file.close()
in_file.close()
