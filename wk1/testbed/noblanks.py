# Get file contents
print '\n'
print 'A Program to Remove Blank Lines:'
print '\n'

targetfile = raw_input('What File would you like to Strip? ')

fd = open(targetfile, 'r')


contents = fd.readlines()
fd.close()

new_contents = []

# Get rid of empty lines
for line in contents:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_contents.append(line)

# Print file sans empty lines
joined = "".join(new_contents)


f = open('Noblanks.txt', 'w')
f.write(joined)
f.close()