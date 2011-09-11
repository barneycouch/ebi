#Extract 18char fasta code from a .fast file:

print '\n'
targetfile = raw_input('Choose a file to extract fasta keys from: ')

infile = open(targetfile, 'r')

fastlist = []
for line in infile:
	line = line.replace("\n", "")
	if line.startswith(">"):
		line = line.replace(">", "")
		fastlist.append(line)
		
fastlist2 = []
for el in fastlist:
	el2 = el[:18]
	fastlist2.append(el2)

print '\n'
print fastlist2

makefile = raw_input('Save a text file of the keys? (y/n):')

if makefile == 'yes':
	
	filename = raw_input('Name the file produced: ')
	
	filer = open(filename, 'w')
	for i in fastlist2:
		filer.write(i)
		filer.write('\n')

