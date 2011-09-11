import numpy as np
from matplotlib.pylab import *
import re
from itertools import groupby
import pylab as P

print '\n'
targetfile = raw_input('What File would you like to Analyse? ')

infile = open(targetfile, 'r')

line = infile.readline()

title = line[1:].rstrip()

sequence_lines = []

while 1:
    line = infile.readline().rstrip()
    if line == "":
        # Reached the end of the record or end of the file
        break
    sequence_lines.append(line)
    if line.startswith(">"):
    	sequence_lines.remove(line)
    	   

sequence_lines2 = []

for space in sequence_lines:
	sequence_lines2.append(re.sub("\n", "", space))
	
a = sequence_lines2
res = [''.join((str(z) for z in y)) for x, y in groupby(a, key = lambda x: len(x) == 60)]
	
sequence_lines3 = []

sequence_lines3 = sequence_lines2

#These Next Two Lines Scare Me:

sequenceraw = "".join(sequence_lines3)

sequence = sequenceraw


afreq = sequence.count('A')
tfreq = sequence.count('T')
ufreq = sequence.count('U')
utfreq = ufreq + tfreq
cfreq = sequence.count('C')
gfreq = sequence.count('G')
nfreq = sequence.count('N')
xfreq = sequence.count('X')
nxfreq = nfreq + xfreq

print '\n'
print 'A appears %g times.' % (afreq)
print 'U or T appears %g times.' % (utfreq)
print 'C appears %g times.' % (cfreq)
print 'G appears %g times.' % (gfreq)
print 'N or X appears %g times.' % (nxfreq)
print '\n'


if tfreq > 0:
	print 'WARNING! THYMINE PRESENT!'
	print '\n'
elif tfreq == 0:
	print 'No Thymine Present.'
	print '\n'

printseq = raw_input('Show The Raw Nucleotide Sequence (y/n)? ')

if printseq == 'y':
	print '\n'
	print 'The Raw Sequence Follows:'
	print '\n'
	print sequence
	print '\n'

printgraph = raw_input('Show A Graph of Nucleotide Frequency (y/n)? ')

if printgraph == 'y':

	print '\n'
	print 'Here is a Graph of Frequency:'
	print '\n'	

	n = 5
	ind = np.arange(n)
	width = 0.35
	basevals = (afreq, utfreq, cfreq, gfreq, nxfreq)
	
	p1 = plt.bar(ind, basevals, width, color='b')
	
	plt.ylabel('Frequency')
	plt.title('Frequency of Bases')
	plt.xticks(ind+width/2., ('A', 'U / T', 'C', 'G', 'N / X') )
	
	plt.show()
	

printhist = raw_input('Show a Histogram of Nucleotide Length (y/n)? ')

if printhist == 'y':
	finalseq = sequence_lines3
	
	forhist = []
	for iter in finalseq:
		afreq2 = iter.count('A')
		tfreq2 = iter.count('T')
		ufreq2 = iter.count('U')
		utfreq2 = ufreq2 + tfreq2
		cfreq2 = iter.count('C')
		gfreq2 = iter.count('G')
		nfreq2 = iter.count('N')
		xfreq2 = iter.count('X')
		nxfreq2 = nfreq2 + xfreq2
		lenseq = afreq2 + utfreq2 + cfreq2 + gfreq2 + nxfreq2
		forhist.append(lenseq)

	x = forhist
	
	# the histogram of the data with histtype='step'
	n, bins, patches = P.hist(x, 50, normed=1, histtype='stepfilled')
	P.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
	
	plt.ylabel('Relative Frequency')
	plt.title('Base Length')
		
	P.show()