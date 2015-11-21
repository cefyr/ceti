#!/usr/bin/env python
# Ceti is a morse code recognition thingy for when the beeps are not enough.
# In the future, it might do more fancy things with command-line options.

import random
import sys
import time

import cetivar as cv

# Default values and thingies
times = 0
letters = cv.letters
random.seed()
stoppit = False

# Figure out language
output_str = cv.output[cv.lang]

def helpAndExit():
    '''Print marginally helpful text and quit'''
    print('Usage: ceti [number of letters]')
    sys.exit()

def convert13Morse(numbers):
    '''Convert the 1-3-code to dots and dashes'''
    output = ''
    for n in range(len(numbers)):
        if numbers[n] == 1:
            output += '.'
        else:
            output += '-'
    return output

def convertMorse13(squiggles):
    '''Convert squiggles from config to 1-3-code'''
    out_array = []
    for n in range(len(squiggles)):
        if squiggles[n] == cv.dotdash[0]:
            out_array += [1]
        elif squiggles[n] == cv.dotdash[1]:
            out_array += [3]
        else:
            print('Error in squiggle conversion')
    return out_array

# Parse arguments
# if len(sys.argv) > 1:
#     if sys.argv[1].isdigit():
#         times = int(sys.argv[1])
#     else:
#         helpAndExit()

start_time = time.monotonic()

# The point should be that you get a prompt of for example -.--
# and the correct answer should be y.
while not stoppit:
    given = ''
    current = random.randint(0,len(letters)-1)
    correct = letters[current][0]
    prompt = convert13Morse(letters[current][1])
    while given != correct:
        given = input('{0} '.format(prompt))
        if given in cv.unknown:
            print(cv.correction[cv.lang].format(correct))
            break
        elif given == cv.stoppit_key:
            stoppit = True
            break
        else:
            times += 1

elapsed_time = time.monotonic() - start_time

print(output_str.format(elapsed_time, elapsed_time/times))
