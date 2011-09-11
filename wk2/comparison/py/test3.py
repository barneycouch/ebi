infile = open('martpl2short.txt', 'r')
tup = []
for line in infile:
	line = line.replace("\n", "")
	tup.append(line)

print '\n'
print tup
print '\n'