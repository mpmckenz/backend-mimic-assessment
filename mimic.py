#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

import random
import sys

def mimic_dict(filename):
    f = open(filename)
    text = f.read()
    word_list =  text.split()
    d = {" ": word_list[0]}
    f.close()
    for i, word in enumerate(word_list):
        if i+1< len(word_list):
            if word in d:
                d[word].append(word_list[i + 1])
            else:
                d[word] = [word_list[i+1]]
    return d
    raise NotImplementedError("Get to Work!")


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
# first random word (key) is empty string, get next random word from that 
# list of values. use tht random word as a key and from that list of value 
# continue to select the next random (key) word

    counter = 0
    for word in mimic_dict:
        if counter<200:
# pass in the key
# print "BEFORE", word
            counter += 1
            word = random.choice(mimic_dict[word])
            return word
# output random value 
# print "AFTER", word, counter
    raise NotImplementedError("Get to Work!")



# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: python mimic.py file-to-read'
        sys.exit(1)

    d = mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
