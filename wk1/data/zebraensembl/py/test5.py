from itertools import groupby

a = ['AAACUTG', 'TTUCAAAAAA', 'CCGGAACTAA', 'CAGGGATTTT', 'TTACCCA']
res = [''.join((str(z) for z in y)) for x, y in groupby(a, key = lambda x: len(x) % 10)]

print res
