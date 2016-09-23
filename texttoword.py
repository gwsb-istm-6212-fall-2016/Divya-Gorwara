#!/usr/bin/env python

"""
A filter that _________.
"""

import fileinput


def process(line):
    """For each line of input, _____."""
    #oneLine = line.rstrip("\n\r")
    oneLine = line
    oneWord = oneLine.split()
    if(len(oneWord) != 0):
        for word in oneWord:
            word = word.strip(',.:')
            if(len(word) >= 2):
                print(word)
    
for line in fileinput.input():
    process(line)
        
