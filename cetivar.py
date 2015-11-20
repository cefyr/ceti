# cetivar.py - variables and strings for ceti

# Configs
times = 10
lang = 'se'


# Language strings
output = {'en': 'Finished in {0:.1f}s ({1:.1f}s/letter)',
          'se': 'Klar på {0:.1f}s ({1:.1f}s/bokstav)'}

correction = {'en': 'Correct: {0}',
              'se': 'Korrekt: {0}'}

helptext = {'en': 'Usage: ceti [number of letters]',
            'se': 'Användning: ceti [antal bokstäver]'} 

# Data
letters = [('a', [1,3]), ('b', [3,1,1,1]), ('c', [3,1,3,1]), ('d', [3,1,1]), 
           ('e', [1]), ('f', [1,1,3,1]), ('g', [3,3,1]), ('h', [1,1,1,1]), 
           ('i', [1,1]), ('j', [1,3,3,3]), ('k', [3,1,3]), ('l', [1,3,1,1]), 
           ('m', [3,3]), ('n', [3,1]), ('o', [3,3,3]), ('p', [1,3,3,1]), 
           ('q', [3,3,1,3]), ('r', [1,3,1]), ('s', [1,1,1]), ('t', [3]), 
           ('u', [1,1,3]), ('ü', [1,1,3,3]), ('v', [1,1,1,3]), ('w', [1,3,3]), 
           ('x', [3,1,1,3]), ('y', [3,1,3,3]), ('z', [3,3,1,1]),
           ('å', [1,3,3,1,3]), ('ä', [1,3,1,3]), ('ö', [3,3,3,1])]

unknown = ['-', ' ', '.']
