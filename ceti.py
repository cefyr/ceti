#!/usr/bin/env python
# Ceti is a morse code recognition thingy for when the beeps are not enough.
# In the future, it might do more fancy things with command-line options.

import random
import sys
import time

import cetivar as cv

# Default values and thingies
times = cv.times
letters = cv.letters
skipped = 0
random.seed()

# Figure out language
output_str = cv.output[cv.lang]

def helpAndExit():
    '''Print marginally helpful text and quit'''
    print('Usage: ceti [number of letters]')
    sys.exit()

def convert13morse(numbers):
    '''Convert the 1-3-code to dots and dashes'''
    output = ''
    for n in range(len(numbers)):
        if numbers[n] == 1:
            output += '.'
        else:
            output += '-'
    return output

#TODO Enable more options and shit
arg = sys.argv[1]
if sys.argv[1].isdigit():
    times = int(sys.argv[1])
else:    
    helpAndExit()

start_time = time.monotonic()

# The point should be that you get a prompt of for example -.-- and the correct
# answer should be y.
for _ in range(times):
    given = ''
    current = random.randint(0,len(letters)-1)
    correct = letters[current][0]
    prompt = convert13morse(letters[current][1])
    while given != correct:
        given = input('{0} '.format(prompt))
        if given in cv.unknown:
            print(cv.correction[cv.lang].format(correct))
            skipped +=1
            break

elapsed_time = time.monotonic() - start_time

print(output_str.format(elapsed_time, elapsed_time/(times - skipped)))
