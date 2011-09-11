#Create a list from the genelist.txt file:

print '\n'
targetfile = 'genelistshort.txt'

infile = open(targetfile, 'r')

line = infile.readline()
genelist = []
for line in infile:
	line = line.replace("\n", "")
	genelist.append(line)

print genelist

#Don't think the following code is useful:

#i2 = []
#for i in genelist:
#	i2.append(str((">") + i))
#print i2


		
