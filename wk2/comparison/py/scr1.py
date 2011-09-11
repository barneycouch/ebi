import Levenshtein

print '\n'
targetfile = 'genelistpl1.txt'

infile = open(targetfile, 'r')

line = infile.readline()
genelist = []
for line in infile:
	line = line.replace("\n", "")
	genelist.append(line)

targetfile2 = 'martpl1.txt'

infile2 = open(targetfile2, 'r')

line2 = infile2.readline()
martlist = []
for line2 in infile2:
	line2 = line2.replace("\n", "")
	martlist.append(line2)

genelistsize = len(genelist)
martlistsize = len(martlist)

print 'The Genelist has %g members.' % (genelistsize)
print 'The Martlist has %g members.' % (martlistsize)
print '\n'

cor = 0

for i in martlist:
	for j in genelist:
		if Levenshtein.ratio(i, j) == 1.0:
			cor = cor + 1	
		if Levenshtein.ratio(i, j) != 1.0:
			cor = cor

print cor
			

