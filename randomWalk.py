import numpy as np
import random
from scipy.special import zeta
import matplotlib.pyplot as plt

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
	lastJump = randomWalk[-1] - randomWalk[-2]

	if drawWalk:
		plt.plot(range(len(randomWalk)), randomWalk)
		if sigma != -1:
			plt.axvline(x=sigma, color='r')
			plt.axhline(y=randomWalk[sigma], color='r')
		plt.show()

	return randomWalk, lastJump

def findConstant(p0, alpha):
	return p0/(zeta(alpha)-zeta(alpha+1))

def findp1(p0, alpha, c):
	return 1+c-c*zeta(alpha)

def findSigma(randomWalk):
	biggestYet = [0 for i in xrange(len(randomWalk))]
	smallestYet = [0 for i in xrange(len(randomWalk))]
	big = randomWalk[-1]
	small = randomWalk[0]
	for i in xrange(len(randomWalk)):
		small = min(small,randomWalk[i])
		big = max(big, randomWalk[-i-1])
		smallestYet[i] = small
		biggestYet[-i-1] = big
	for i in xrange(len(randomWalk)):
		if (smallestYet[i] >= biggestYet[i]):
			return i
	return -1

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

def getStepSize(dist):
	r = np.random.uniform()
	for x in dist:
		if r < x:
			return dist.index(x)-1
	return len(dist)-1

def generateRandomWalks(n = 100, p0 = 0.5, alpha = 1.5):
	CalcSum = 0
	for i in xrange(10):
		K = RandomWalk(n, p0, alpha, drawWalk = False)
		lastJump = K[1]
		CalcSum += np.log(float(lastJump)/n)
	return CalcSum/n

n = 10000
p0 = 0.5
alpha = 1.5
randomwalk = RandomWalk(n,p0,alpha)
