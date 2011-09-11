targetfile = raw_input('What File would you like? ')

infile = open(targetfile, 'r')

line = infile.readline()

if not line.startswith(">"):
    raise TypeError("Not a FASTA file: %r" % line)

sequence_lines = []
while 1:
    line = infile.readline().rstrip()
    if line == "":
        # Reached the end of the record or end of the file
        break
    sequence_lines.append(line)
    
sequenceraw = "".join(sequence_lines)

#CHANGE THIS LINE WHEN I GET A GOOD ALGORITHM!
sequence = sequenceraw

afreq = sequence.count('A')
tfreq = sequence.count('T')
ufreq = sequence.count('U')
utfreq = ufreq + tfreq
cfreq = sequence.count('C')
gfreq = sequence.count('G')

print 'A appears %g times.' % (afreq)
print 'U or T appears %g times.' % (utfreq)
print 'C appears %g times.' % (cfreq)
print 'G appears %g times.' % (gfreq)

if tfreq > 0:
	print 'WARNING! THYMINE PRESENT!'
elif tfreq == 0:
	print 'No Thymine Present.'

printseq = raw_input('Show The Sequence (y/n)? ')

if printseq == 'y':
	print 'The Sequence Follows:'
	print sequence

maxfreq = max(afreq, utfreq, cfreq, gfreq)
divfactor = maxfreq
roundpoint = 2

print 'Here is a Graph of Frequency:'

import numpy as np
from matplotlib.pylab import *

max = maxfreq
rawint = max/10.0
proint = round(rawint, -2)
n = 4
ind = np.arange(n)
width = 0.35
basevals = (afreq, utfreq, cfreq, gfreq)

p1 = plt.bar(ind, basevals, width, color='b')

plt.ylabel('Frequency')
plt.title('Frequency of Bases')
plt.xticks(ind+width/2., ('A', 'U / T', 'C', 'G') )
plt.yticks(np.arange(0,(max+proint),proint))

plt.show()
