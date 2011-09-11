string = ['AAAACGGTTT', 'AACCGGGTT', 'AACCCUUTTT', 'AAAAACTTTU', 'AAACATTTTU', 'TAAAATTTTU']
indyes = []
indnot = []
print string
for l in string:
	if not len(l) % 10:
		indyes2 = string.index(l)
		indyes.append(indyes2)
		print 'Victory.'
		print 'Index is %g.' % (string.index(l))
		ac = l.count('A')
		tc = l.count('T')
		cc = l.count('C')
		uc = l.count('U')
		gc = l.count('G')
		count = ac + tc + cc + uc + gc
		print 'NT Length is %g' % (count)
	elif len(l) % 10:
		indnot2 = string.index(l)
		indnot.append(indnot2)
		print 'Loss.'
		print 'Index is %g.' % (string.index(l))
		ac = l.count('A')
		tc = l.count('T')
		cc = l.count('C')
		uc = l.count('U')
		gc = l.count('G')
		count = ac + tc + cc + uc + gc
		print 'NT Length is %g' % (count)		
		
print 'Raw String:'
print '\n'
print string
print '\n'
print 'Full Line Indexes:'
print '\n'
print indyes
print '\n'
print 'Part Line Indexes:'
print '\n'
print indnot
print '\n'

str2 = []

for r in indyes:
	ite = indyes.index(r)
	ine = ite + 1
	print 'i.t.e - %g' %(ite)
	print 'i.n.e - %g' %(ine)	
	print '\n'
	nextval = r + 1
	if nextval in indyes:
		str2[ite] += str2.pop(ine)
		
print str2