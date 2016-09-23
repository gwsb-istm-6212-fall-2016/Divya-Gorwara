#!/usr/bin/env python

"""
A filter that _________.
"""

import fileinput


def process(line):
    """For each line of input, _____."""
    oneWord = line.split()
    for word in oneWord:
        print(word.lower())
    
for line in fileinput.input():
    process(line)
        
