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
    	   
import re

sequence_lines2 = []

for space in sequence_lines:
	sequence_lines2.append(re.sub("\n", "", space))
	
sequence_lines3 = []

sequence_lines3 = sequence_lines2

sequence_lines4 = []

for item in sequence_lines3:
	sequence_lines4.append(re.sub("A*$", "", item))

print sequence_lines2
print sequence_lines3
print sequence_lines3
print sequence_lines4


sequenceraw = "".join(sequence_lines4)

#CHANGE THIS LINE WHEN I GET A GOOD ALGORITHM!
sequence = sequenceraw

afreq = sequence.count('A')
tfreq = sequence.count('T')
ufreq = sequence.count('U')
utfreq = ufreq + tfreq
cfreq = sequence.count('C')
gfreq = sequence.count('G')

print '\n'
print 'A appears %g times.' % (afreq)
print 'U or T appears %g times.' % (utfreq)
print 'C appears %g times.' % (cfreq)
print 'G appears %g times.' % (gfreq)
print '\n'


afreq = sequence.count('A')
tfreq = sequence.count('T')
ufreq = sequence.count('U')
utfreq = ufreq + tfreq
cfreq = sequence.count('C')
gfreq = sequence.count('G')



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

	import numpy as np
	from matplotlib.pylab import *

	n = 4
	ind = np.arange(n)
	width = 0.35
	basevals = (afreq, utfreq, cfreq, gfreq)
	
	p1 = plt.bar(ind, basevals, width, color='b')
	
	plt.ylabel('Frequency')
	plt.title('Frequency of Bases')
	plt.xticks(ind+width/2., ('A', 'U / T', 'C', 'G') )
	
	plt.show()

	print '\n'	
	print 'End of Program.'
	print '\n'	
	
elif printgraph == 'n':
	print '\n'
	print 'End of Program.'
	print '\n'
