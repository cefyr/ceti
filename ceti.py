#!/usr/bin/env python
# Ceti is a morse code recognition thingy for when the beeps are not enough.
# In the future, it might do more fancy things with command-line options.

import random
import sys
import time
import argparse
import curses

import cetivar as cv

# Default values and thingies
times = 0
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

# argparse handles sysargs
# letters to dot/dash or dot/dash to letters
## group: -t --to -f --from
# just letters or whole words/sentences
## group: -l --letters -w --words -s --sentences
# translate from file
## -F --file <file> [or - from STDIN]  
# letters, numbers and/or punctuation
## -a --alphabet
## -n --numbers
## -p --punctuation
parser = argparse.ArgumentParser(description=cv.description)
# One of these must be used
translate_group = parser.add_mutually_exclusive_group(required=True)
translate_group.add_argument("-t", "--to", action="store_true", help=cv.arg_to)
translate_group.add_argument("-f", "--from", action="store_true", help=cv.arg_from)
# This one is optional but needs a path or - for stdin
#parser.add_argument("-F", "--file", nargs="?", default=sys.stdin, type=argparse.FileType('r'), help=cv.arg_file)
# At least one of these must exist
parser.add_argument("source", nargs='*', help=cv.arg_source)
# source_group = 
# source_group.add_argument("-a", "--alphabet", action="store_true", 
#                           help=cv.arg_alphabet)
# source_group.add_argument("-n", "--numbers", action="store_true", 
#                           help=cv.arg_numbers)
# source_group.add_argument("-p", "--punctuation", action="store_true", 
#                           help=cv.arg_punctuation)
args = parser.parse_args()
# to OR from is True
# filename is optional but not implemented
# there is some combination of a, n and/or p in source

# Debug test of sysargs
if args.to:
    print('letters -> morse')
else:
    print('morse -> letters')
print(args.source)

# Handle letters/numbers/punctuation marks
signs = []
if 'l' in args.source[0]:
    signs += cv.letters
if 'n' in args.source[0]:
    signs += cv.numbers
if 'p' in args.source[0]:
    signs += cv.punctuation
if len(signs) == 0:
    print('ERROR: Nothing todooo, use args l/n/p')
    sys.exit()

start_time = time.monotonic()

# The point should be that you get a prompt of for example -.--
# and the correct answer should be y.
while not stoppit:
    given = ''
    current = random.randint(0,len(signs)-1)
    correct = signs[current][0]
    prompt = convert13Morse(signs[current][1])
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
#TODO handle ZeroDivisionError for when you give up at once
