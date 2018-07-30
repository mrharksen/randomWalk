import numpy as np
import random
from scipy.special import zeta
import matplotlib.pyplot as plt


def randomSticks(n = 100, p0 = 0.5, alpha = 1.5, drawWalk = True, drawSticks = True):
	c = findConstant(p0,alpha)
	p1 = findp1(p0,alpha,c)
	dist = Distribution(p0, p1, alpha, c)
	randomWalk = [0 for i in xrange(n)]
	length = n
	cnt = 0
	index = 0
	while(cnt < n):
		index += 1
		step = getStepSize(dist)
		if( step >= 0):
			cnt += 1
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
		if drawSticks:
			tops, bottoms, xjumps = jumps(randomWalk, n)
			for i in range(len(xjumps)):
				x = (xjumps[i]+1, xjumps[i]+1)
				y = (bottoms[i], tops[i])
				plt.plot(x, y,  'C1')
			tops, bottoms, xjumps = removeSticks(tops, bottoms, xjumps, n)
			sticksleft = len(tops)
			print sticksleft
			for i in range(len(xjumps)):
				x = (xjumps[i]+1, xjumps[i]+1)
				y = (bottoms[i], tops[i])
				plt.plot(x, y,  'C4')
		plt.show()

	return randomWalk


def jumps(randomWalk, n):
	tops = [0 for i in xrange(n)]
	bottoms = [0 for i in xrange(n)]
	xjumps = [0 for i in xrange(n)]
	cnt = 0;
	for i in xrange(len(randomWalk)-1):
		if randomWalk[i+1] >= randomWalk[i]:
			bottoms[cnt] = randomWalk[i]
			tops[cnt] = randomWalk[i+1]
			xjumps[cnt] = i
			cnt = cnt + 1
	return tops, bottoms, xjumps

'''
def jumpTops(randomWalk, n):
	tops = [0 for i in xrange(n)]
	cnt = 0;
	for i in xrange(len(randomWalk)-1):
		if randomWalk[i+1] >= randomWalk[i]:
			tops[cnt] = randomWalk[i+1]
			cnt = cnt + 1
	return tops


def jumpBottoms(randomWalk):
	bottoms = [0 for i in xrange(n)]
	cnt = 0;
	for i in xrange(len(randomWalk)-1):
		if randomWalk[i+1] >= randomWalk[i]:
			bottoms[cnt] = randomWalk[i]
			cnt = cnt + 1
	return bottoms
'''

def rightShadow(tops, bottoms, i, n):
	TOP = tops[i]
	BOTTOM = bottoms[i]
	shadow = [0 for j in xrange(n)]
	count = 0
	for j in xrange(i+1,i+n):
		j = j % n
		if TOP < BOTTOM:
			break
		if bottoms[j] >= BOTTOM and tops[j] <= TOP:
			shadow[j] = 1
		else:
			if bottoms[j] < BOTTOM and tops[j] > TOP:
				break
			if bottoms[j] < BOTTOM and tops[j] > BOTTOM:
				BOTTOM = tops[j]
			if bottoms[j] < TOP and tops[j] > TOP:
				TOP = bottoms[j]
	return shadow


def leftShadow(tops, bottoms, i, n):
	TOP = tops[i]
	BOTTOM = bottoms[i]
	shadow = [0 for j in xrange(n)]
	count = 0
	for j in xrange(i-1,i-n+2,-1):
		j = j % n
		if TOP < BOTTOM:
			break
		if bottoms[j] >= BOTTOM and tops[j] <= TOP:
			shadow[j] = 1
		else:
			if bottoms[j] < BOTTOM and tops[j] > TOP:
				break
			if bottoms[j] < BOTTOM and tops[j] > BOTTOM:
				BOTTOM = tops[j]
			if bottoms[j] < TOP and tops[j] > TOP:
				TOP = bottoms[j]
	return shadow


def removeSticks(tops, bottoms, xjumps, n):
	sticks = [1 for i in xrange(n)]
	for i in xrange(n):
		if sticks[i] == 1:
			skuggar = leftShadow(tops, bottoms, i, n)
			for j in xrange(n):
				j= j % n
				if skuggar[j] == 1:
					sticks[j] = 0
	noRemaining = sum(sticks)
	newTops = [0 for i in xrange(noRemaining)]
	newBottoms = [0 for i in xrange(noRemaining)]
	newXjumps = [0 for i in xrange(noRemaining)]
	cnt = 0
	for i in xrange(n):
		if sticks[i] == 1:
			newTops[cnt] = tops[i]
			newBottoms[cnt] = bottoms[i]
			newXjumps[cnt] = xjumps[i]
			cnt = cnt + 1
	return newTops, newBottoms, newXjumps


def whoRemove(tops, bottoms, xjumps, n):
	sticks = [1 for i in xrange(n)]
	for i in xrange(n):
		if sticks[i] == 1:
			skuggar = leftShadow(tops, bottoms, i, n)
			for j in xrange(n):
				j= j % n
				if skuggar[j] == 1:
					sticks[j] = 0
	return sticks
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
	n = 10000
	p0 = 0.5
	alpha = 1.5
	rnd = randomSticks(n,p0,alpha)
	tops, bottoms, xjumps = jumps(rnd, n)
	#tops = jumpTops(rnd)
	#bottoms = jumpBottoms(rnd)
'''
	print str(rnd)

	for i in xrange(n):
		print str(bottoms[i])+" -> "+str(tops[i])

	for i in xrange(n):
		print inShadow(tops, bottoms, i, n)

	print "og svo kemur: "+str(removeSticks(tops, bottoms, n))
'''
if __name__ == "__main__":
	main()
