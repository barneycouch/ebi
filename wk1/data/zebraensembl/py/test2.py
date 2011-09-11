import numpy as np
from matplotlib.pylab import *

finalseq = ['AAACUTG', 'TTUCAAAAAAAA', 'CCGGAACT', 'CAGGGATTTT']
forhist = []
for iter in finalseq:
	afreq2 = iter.count('A')
	tfreq2 = iter.count('T')
	ufreq2 = iter.count('U')
	utfreq2 = ufreq2 + tfreq2
	cfreq2 = iter.count('C')
	gfreq2 = iter.count('G')
	lenseq = afreq2 + utfreq2 + cfreq2 + gfreq2
	print lenseq
	forhist.append(lenseq)
	print '\n'

print forhist