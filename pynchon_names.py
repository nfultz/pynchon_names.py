#! /usr/bin/env python
"""
    Usage: ./pynchon_names.py [number]"

    Copyright (C) 2007, Christopher Swingley
    Licensed under term of GNU General Public License v.2.0

    NOTE: Replace WORD_DICTIONARY with your word list (one word
        per line in the file)
"""

import random, string, sys, re

WORD_DICTIONARY = "/usr/share/dict/words"

if len(sys.argv) > 1:
    number = int(sys.argv[1])
else:
    number = 10

def cssstrip(foo):
    bar = foo.lower().strip()
    bar = re.sub("\W", "", bar)
    return bar

words = open(WORD_DICTIONARY).readlines()

for i in range(number):
    first_word = ""
    second_word = ""
    while len(first_word) > 7 or len(first_word) < 2:
        first_word = cssstrip(random.choice(words))
    first_word_len = len(first_word)
    while len(second_word) + first_word_len > 12 or len(second_word) + first_word_len < 5 or len(second_word) < 2:
        second_word = cssstrip(random.choice(words))

    print "%s%s%s %s%s%s" % (first_word[0].upper(), first_word[1:], second_word, second_word[0].upper(), second_word[1:], first_word)

