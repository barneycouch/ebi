import numpy as np
import pylab as P

foo = [7, 12, 11, 8, 8, 8, 8, 10]

sigma = np.std(foo)
mu = np.mean(foo)
x = foo

# the histogram of the data with histtype='step'
n, bins, patches = P.hist(x, 50, normed=1, histtype='stepfilled')
P.setp(patches, 'facecolor', 'r', 'alpha', 0.75)

# add a line showing the expected distribution
y = P.normpdf( bins, mu, sigma)
l = P.plot(bins, y, 'k--', linewidth=1.5)


P.show()