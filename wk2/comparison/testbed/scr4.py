targfile = raw_input('Which File holds the affy/fasta conversion data? ')
infile = open(targfile, 'r') #martlist shows all corresponding affy/fasta ids

alist = []
blist = []

for line in infile:
	a, b = [x for x in line.split()]
	alist.append(a)
	blist.append(b)
	
#alist contains all ensembl ids
#blist contains all affy ids

print '\n'
targfile2 = raw_input('Which File holds the identified affy codes? ')
infile2 = open(targfile2, 'r') #genelist contains the identified affy codes

glist = []
for line2 in infile2:
	line2 = line2.replace("\n", "")
	glist.append(line2)

#glist contains clean formatted affy codes from genelist

print '\n'
print 'Checking for matches... (1 of 2)'
print '\n'

eids = []
indexes = []
print 'Matches found: '
for i in glist:
	for z in blist:
		inde = glist.index(i)
		ind = blist.index(z)
		if i == z:
			print i
			indexes.append(inde)
			eidsappend = alist.pop(ind)
			eids.append(eidsappend)

print '\n'
print 'Checking for matches... (2 of 2) '
print '\n'			

relevantdrs = []
for i in indexes:
	drindex = glist.pop(i)
	relevantdrs.append(drindex)
			
#where there is a match between the identified affys and the database, store the ensembl id in eids

targfile3 = raw_input('Which File contains the ensembl identifiers and nucleotide sequences? ')
infile = open(targfile3, 'r') #esh contains all the nucleotide sequences with relevant ensembl ids

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
		

fastants2 = []
for newer in fastants:
		newer2 = newer.replace("\n", "")
		fastants2.append(newer2)
		
#fastaids contains a list of all the ensembl ids in the ensembl database
#fastants2 contains a formatted list of all the nucleotide sequences in esh 
		
ntforfast = [] #the set to put the relevant nt sequences in for the final fasta file
		
#eids contains the ensembl ids of a match
		
for ish in eids:
	for esh in fastaids:
		if ish == esh:
			ind2 = eids.index(ish)
			ntforfast.append(fastants.pop(ind2))

ntforfast2 = []			
for news in ntforfast:
		news2 = news.replace("\n", "")
		ntforfast2.append(news2)

filename = raw_input('Name the file to save information to: ')
filer = open(filename, 'w')

for i in relevantdrs:
	filer.write('>%s' % (i))
	filer.write('\n')
	indrel = relevantdrs.index(i)
	filer.write(ntforfast2.pop(indrel))
	filer.write('\n')
	