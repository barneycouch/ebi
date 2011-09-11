#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import os, sys, re

if len(sys.argv) != 4:
	print "need <affy file>  <map file>  <fasta file> arguments"
	exit(1)

idfile, mapfile, fastafile = sys.argv[1:4]

print idfile, mapfile, fastafile

maphandle = open(mapfile, 'r') #martlist shows all corresponding affy/fasta ids

affy_to_ens = {}

for line in maphandle:
	# a, b = [x for x in line.split()]
	a, b = line.split()
	affy_to_ens[b] = a
	print "map %s to %s" % (b, a)
maphandle.close()

idhandle = open(idfile, 'r') #genelist contains the identified affy codes

# glist contains clean formatted affy codes from genelist
glist = []

for line in idhandle:
	line = line.replace("\n", "")
	glist.append(line)
idhandle.close()

fastahandle = open(fastafile, 'r')
# fastadb contains all the nucleotide sequences indexed by the relevant ensembl id

fastadb = {}
curid = ""

lnum = 0
for line in fastahandle:
	lnum += 1
	if lnum % 2:
		rer = re.search(r'^>(\S*)\s', line, re.IGNORECASE)
		if rer:
			curid = rer.group(1)
		else:
			print "parse error in line %s" % (line)
			exit(1)
		print(curid)
		fastadb[curid] = ""
	elif not lnum % 2:
		fastadb[curid] += line
idhandle.close()

fpout = open("ttt.txt", 'w')

for a in glist:
	if not a in affy_to_ens:
		print "affy identifier %s not found in mapping" % (a)
		continue
	e = affy_to_ens[a]
	print "testing %s" % (e)
	if not e in fastadb:
		print "ensembl/affy %s/%s not found in fasta repository" % (e,a)
		continue

	fpout.write(">%s\n%s" % (a, fastadb[e]))

