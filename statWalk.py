import numpy as np
import scipy.stats as stats
import pylab as pl

a40b = np.loadtxt('alpha_40n100.txt')
pl.hist(a40b,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.4$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat40b, pval40b =  stats.normaltest(a40b)
print 'alpha = 1.4 and n = 100'
print 'pval = ' + str(pval40b)
print 'mean = ' + str(np.mean(a40b))
print 'samplesize = ' + str(len(a40b)) + '\n'

a40 = np.loadtxt('alpha_40.txt')
pl.hist(a40,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.4$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat40, pval40 =  stats.normaltest(a40)
print 'alpha = 1.40 and n = 1000'
print 'pval = ' + str(pval40)
print 'mean = ' + str(np.mean(a40))
print 'samplesize = ' + str(len(a40)) + '\n'

a45b = np.loadtxt('alpha_45n100.txt')
pl.hist(a45b,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.45$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat45b, pval45b =  stats.normaltest(a45b)
print 'alpha = 1.45 and n = 100'
print 'pval = ' + str(pval45b)
print 'mean = ' + str(np.mean(a45b))
print 'samplesize = ' + str(len(a45b)) + '\n'

a45 = np.loadtxt('alpha_45.txt')
pl.hist(a45,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.45$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat45, pval45 =  stats.normaltest(a45)
print 'alpha = 1.45 and n = 1000'
print 'pval = ' + str(pval45)
print 'mean = ' + str(np.mean(a45))
print 'samplesize = ' + str(len(a45)) + '\n'

a50b = np.loadtxt('alpha_50n100.txt')
pl.hist(a50b,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.5$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat50b, pval50b =  stats.normaltest(a50b)
print 'alpha = 1.5 and n = 100'
print 'pval = ' + str(pval50b)
print 'mean = ' + str(np.mean(a50b))
print 'samplesize = ' + str(len(a50b)) + '\n'

a50d = np.loadtxt('alpha_50n200.txt')
pl.hist(a50d,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.5$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat50d, pval50d =  stats.normaltest(a50d)
print 'alpha = 1.5 and n = 200'
print 'pval = ' + str(pval50d)
print 'mean = ' + str(np.mean(a50d))
print 'samplesize = ' + str(len(a50d)) + '\n'

a50e = np.loadtxt('alpha_50n300.txt')
pl.hist(a50e,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.5$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat50e, pval50e =  stats.normaltest(a50e)
print 'alpha = 1.5 and n = 300'
print 'pval = ' + str(pval50e)
print 'mean = ' + str(np.mean(a50e))
print 'samplesize = ' + str(len(a50e)) + '\n'

a50 = np.loadtxt('alpha_50.txt')
pl.hist(a50,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.5$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat50, pval50 =  stats.normaltest(a50)
print 'alpha = 1.5 and n = 1000'
print 'pval = ' + str(pval50)
print 'mean = ' + str(np.mean(a50))
print 'samplesize = ' + str(len(a50)) + '\n'

a50c = np.loadtxt('alpha_50n10000.txt')
pl.hist(a50c,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.5$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat50c, pval50c =  stats.normaltest(a50c)
print 'alpha = 1.5 and n = 10000'
print 'pval = ' + str(pval50c)
print 'mean = ' + str(np.mean(a50c))
print 'samplesize = ' + str(len(a50c)) + '\n'

a55b = np.loadtxt('alpha_55n100.txt')
pl.hist(a55b,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.55$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat55b, pval55b =  stats.normaltest(a55b)
print 'alpha = 1.55 and n = 100'
print 'pval = ' + str(pval55b)
print 'mean = ' + str(np.mean(a55b))
print 'samplesize = ' + str(len(a55b)) + '\n'

a55 = np.loadtxt('alpha_55.txt')
pl.hist(a55,normed=True, bins=15)
pl.title('For ' + r'$ \alpha = 1.55$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat55, pval55 =  stats.normaltest(a55)
print 'alpha = 1.55 and n = 1000'
print 'pval = ' + str(pval55)
print 'mean = ' + str(np.mean(a55))
print 'samplesize = ' + str(len(a55)) + '\n'

a60b = np.loadtxt('alpha_60n100.txt')
pl.hist(a60b,normed=True,bins=15)
pl.title('For ' + r'$ \alpha = 1.6$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat60b, pval60b =  stats.normaltest(a60b)
print 'alpha = 1.60 and n = 100'
print 'pval = ' + str(pval60b)
print 'mean = ' + str(np.mean(a60b))
print 'samplesize = ' + str(len(a60b)) + '\n'

a60 = np.loadtxt('alpha_60.txt')
pl.hist(a60,normed=True,bins=15)
pl.title('For ' + r'$ \alpha = 1.6$')
pl.ylabel("Probability")
pl.xlabel("Value of $\log(\Delta_R / n )$")
pl.show()
stat60, pval60 =  stats.normaltest(a60)
print 'alpha = 1.60 and n = 1000'
print 'pval = ' + str(pval60)
print 'mean = ' + str(np.mean(a60))
print 'samplesize = ' + str(len(a60)) + '\n'
