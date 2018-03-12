#!/usr/bin/python

import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv[1])

if '^3' in str(sys.argv[1]):
    print 'Not possible'
else:
    print 245435433343434.20 ** (0.5)
