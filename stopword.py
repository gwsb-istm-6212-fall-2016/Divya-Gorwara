#!/usr/bin/env python

"""
A filter that _________.
"""

import fileinput


def process(line):
    """For each line of input, _____."""
    stopword = ['a', 'an', 'of', 'is', 'was', 'to', 'at', 'it', 'or', 'will']
    oneLine = line.rstrip("\n\r")
    oneWord = oneLine.split()
    if(len(oneWord) != 0):
        for word in oneWord:
            word = word.lower()
            word = word.strip(',.:')
            if(word not in stopword):
                print(word)

for line in fileinput.input():
    process(line)
        
