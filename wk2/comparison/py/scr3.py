#Extract 18char fasta code from a .fast file:

print '\n'
targetfile = raw_input('Choose a file to extract fasta keys from: ')

infile = open(targetfile, 'r')

fastlist = []
for line in infile:
	line = line.replace("\n", "")
	fastlist.append(line)
		
fastlist2 = [] #fastlist2 = list of 18char ids
for el in fastlist:
	if el.startswith(">"):
		el = el.replace(">", "")
		el = el[:18]
		fastlist2.append(el)
	elif not el.startswith(">"):
		fastlist2.append(el)

makefile = raw_input('Save a text file of the keys? (y/n):')

if makefile == 'y':
	
	filename = raw_input('Name the file produced: ')
	
	filer = open(filename, 'w')
	for i in fastlist2:
		filer.write(i)
		filer.write('\n')

#Tuplify the codes and nucleotide sequences:

i = iter(fastlist2)
fastlist3 = zip(i, i)

for a in fastlist3:
	for b in a:
		print b