__author__ = 'vera'

import re

fname = raw_input("Enter the file name:")
handle = open(fname)

sum = 0

for line in handle:
    for item in re.findall('([0-9]+)',line):
        sum = sum + int(item)

print sum
