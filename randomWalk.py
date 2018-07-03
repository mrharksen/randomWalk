import numpy as np
import random
from scipy.special import zeta
import matplotlib.pyplot as plt


'''
	Input:
			n         integer    the starting point of the random walk.
			p0        float      in (0,1) corresponding to probability of going down 1.
			alpha     float      in (1,2) corresponding to exponent of distribution.
			drawWalk  boolean    if True then the random walk is drawn.

	Output:
            randomWalk   integer list    keeps track of the height of the random walk.

	Usage:
	        randomWalk = RandomWalk(10000, 0.4, 1.4, False)

    Description:
	        We have two conditions:

			      p0 + p1 + p2 + ... = 1
				  0*p0 + 1*p1 + ... = 1

		where p0 is a given probability corresponding to taking one
		step down in the random walk, p1 is found by the conditions above.
        The rest of the probabilities follow pi ~ c*i^{-(alpha+1)} where alpha
		is the given input above. The constant c is found by the conditions above.

        We start by generating a random walk which starts at height n and stops
		when it reaches zero. Then we find the first step of the walk such that
		all steps before are higher and all steps below are lower. We call that step
		sigma. Then we continue generating the random walk until we reach a height
		higher than the height which the random walk had at sigma.
'''
def RandomWalk(n = 1000, p0 = 0.5, alpha = 1.5, drawWalk = True):
	c = findConstant(p0,alpha)
	p1 = findp1(p0,alpha,c)
	dist = Distribution(p0, p1, alpha, c)
	randomWalk = [0 for i in xrange(n)]
	randomWalk[0] = n
	length = n
	index = 0
	while(randomWalk[index] > 0):
		index += 1
		step = getStepSize(dist)
		if(index == length):
			length *= 2
			temp = [0 for i in xrange(length)]
			for i in xrange(length/2):
				temp[i] = randomWalk[i]
			del randomWalk
			randomWalk = temp
		randomWalk[index] = randomWalk[index-1]+step
	sigma = findSigma(randomWalk)
	sigmaHeight = randomWalk[sigma]
	while(randomWalk[index] < sigmaHeight):
		index += 1
		step = getStepSize(dist)
		if(index == length):
			length *= 2
			temp = [0 for i in xrange(length)]
			for i in xrange(length/2):
				temp[i] = randomWalk[i]
			del randomWalk
			randomWalk = temp
		randomWalk[index] = randomWalk[index-1]+step
	randomWalk = randomWalk[:index+1]

	if drawWalk:
		plt.plot(range(len(randomWalk)), randomWalk)
		if sigma != -1:
			plt.axvline(x=sigma, color='r')
			plt.axhline(y=randomWalk[sigma], color='r')
		plt.show()

	return randomWalk

'''
    Finds the constant c by the conditions above.
'''

def findConstant(p0, alpha):
	return p0/(zeta(alpha)-zeta(alpha+1))

'''
    Finds the probability p1 by the conditions above.
'''
def findp1(p0, alpha, c):
	return 1+c-c*zeta(alpha)
'''
   Finds the point sigma as described above.
'''
def findSigma(randomWalk):
	biggestYet = [0 for i in xrange(len(randomWalk))]
	smallestYet = [0 for i in xrange(len(randomWalk))]
	big = randomWalk[-1]
	small = randomWalk[0]
	for i in xrange(len(randomWalk)):
		small = min(small,randomWalk[i]) #keeps track of the lowest element encountered.
		big = max(big, randomWalk[-i-1]) #keeps track of the largest element encountered.
		smallestYet[i] = small
		biggestYet[-i-1] = big
	for i in xrange(len(randomWalk)):
		if (smallestYet[i] >= biggestYet[i]):
			return i
	return -1 #no element found.

'''
    Generates the distribution function of the corresponding probabilities
	p0, p1, ... such that sum pi > 0.99999999 (which can be altered).
'''
def Distribution(p0, p1, alpha, c):
	invDist = []
	invDist.append(p0)
	invDist.append(p0+p1)
	cumsum = p0+p1
	j = 1
	while(0.99999999 > cumsum):
		cumsum += c*np.power((j+1),-(alpha+1))
		invDist.append(cumsum)
		j += 1
	return invDist

'''
    Finds the size of the step which the random walk takes next.
'''
def getStepSize(dist):
	r = np.random.uniform()
	for x in dist:
		if r < x:
			return dist.index(x)-1
	return len(dist)-1

def main():
	n = 1000
	p0 = 0.5
	alpha = 1.5
	randomwalk = RandomWalk(n,p0,alpha)

if __name__ == "__main__":
	main()
