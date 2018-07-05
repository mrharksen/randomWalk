import numpy as np
import random
from scipy.special import zeta
import matplotlib.pyplot as plt
import randomWalk

def WalkGenerator(n, p0, alpha, filename):
    randWalk = randomWalk.RandomWalk(n,p0,alpha,drawWalk = False)
    lastJump = randWalk[-1] - randWalk[-2]
    SumVal = np.log(float(lastJump)/n)
    with open(filename, 'a') as file:
        file.write(str(SumVal) + '\n')

n = 300
p0 = 0.5

alpha_05 = 1.05
alpha_10 = 1.10
alpha_15 = 1.15
alpha_20 = 1.20
alpha_25 = 1.25
alpha_30 = 1.30
alpha_35 = 1.35
alpha_40 = 1.40
alpha_45 = 1.45
alpha_50 = 1.50
alpha_55 = 1.55
alpha_60 = 1.60
alpha_65 = 1.65
alpha_70 = 1.70
alpha_75 = 1.75
alpha_80 = 1.80
alpha_85 = 1.85
alpha_90 = 1.90
alpha_95 = 1.95

talpha_05 = "alpha_05n10000.txt"
talpha_10 = "alpha_10n10000.txt"
talpha_15 = "alpha_15n10000.txt"
talpha_20 = "alpha_20n10000.txt"
talpha_25 = "alpha_25n10000.txt"
talpha_30 = "alpha_30n10000.txt"
talpha_35 = "alpha_35n10000.txt"
talpha_40 = "alpha_40n10000.txt"
talpha_45 = "alpha_45n10000.txt"
talpha_50 = "alpha_50n300.txt"
talpha_55 = "alpha_55n10000.txt"
talpha_60 = "alpha_60n10000.txt"
talpha_65 = "alpha_65n10000.txt"
talpha_70 = "alpha_70n10000.txt"
talpha_75 = "alpha_75n10000.txt"
talpha_80 = "alpha_80n10000.txt"
talpha_85 = "alpha_85n10000.txt"
talpha_90 = "alpha_90n10000.txt"
talpha_95 = "alpha_95n10000.txt"

for i in xrange(10):
#WalkGenerator(n, p0, alpha_05, talpha_05)
#WalkGenerator(n, p0, alpha_10, talpha_10)
#WalkGenerator(n, p0, alpha_15, talpha_15)
#WalkGenerator(n, p0, alpha_20, talpha_20)
#WalkGenerator(n, p0, alpha_25, talpha_25)
#WalkGenerator(n, p0, alpha_30, talpha_30)
#WalkGenerator(n, p0, alpha_35, talpha_35)
    #WalkGenerator(n, p0, alpha_40, talpha_40)
    #WalkGenerator(n, p0, alpha_45, talpha_45)
    WalkGenerator(n, p0, alpha_50, talpha_50)
    #WalkGenerator(n, p0, alpha_55, talpha_55)
    #WalkGenerator(n, p0, alpha_60, talpha_60)
#WalkGenerator(n, p0, alpha_65, talpha_65)
#WalkGenerator(n, p0, alpha_70, talpha_70)
#WalkGenerator(n, p0, alpha_75, talpha_75)
#WalkGenerator(n, p0, alpha_80, talpha_80)
#WalkGenerator(n, p0, alpha_85, talpha_85)
#WalkGenerator(n, p0, alpha_90, talpha_90)
#WalkGenerator(n, p0, alpha_95, talpha_95)
