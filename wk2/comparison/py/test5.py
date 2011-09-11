infile = open('esh.fasta', 'r')

fastaids = []
fastants = []

lnum = 2
for line in infile:
	lnum += 1
	if lnum % 2:
		line = line.replace(">", "")
		line = line[:18]
		fastaids.append(line)
	elif not lnum % 2:
		fastants.append(line)
		
