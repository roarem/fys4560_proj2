import numpy as np
import matplotlib.pyplot as plt

inFile = open("zTopCross.txt",'r')
process = inFile.readline()
xaxis   = inFile.readline()
title   = inFile.readline()
inFile.close()

sqrtSAsym, Asymmetry = np.loadtxt('zTopAsym.txt',unpack=True,skiprows=3)
sqrtSCross, crosSection = np.loadtxt('zTopCross.txt',unpack=True,skiprows=3)
#ZMAsym  = [[91,91],[np.min(Asymmetry),np.max(Asymmetry)]]
#ZMCross = [[91,91],[np.min(crosSection),np.max(crosSection)]]
#ZpMAsym  = [[1000,1000],[np.min(Asymmetry),np.max(Asymmetry)]]
#ZpMCross = [[1000,1000],[np.min(crosSection),np.max(crosSection)]]

fig, ax = plt.subplots()

ax.plot(sqrtSAsym, Asymmetry)
#ax.plot(ZMAsym[0],ZMAsym[1],label="Z mass")
#ax.plot(ZpMAsym[0],ZpMAsym[1],label="Z' mass")
#ax.legend(loc='best')
ax.set_xlabel(r'$\sqrt{s}$ [GeV]')
ax.set_ylabel('Asymmetry')
plt.savefig('ZAsym.pdf')
#ax[0].text(x=91,y=0.6,s="Z")
#ax[0].text(x=1000,y=0.6,s="Z'")

fig, ax = plt.subplots()
ax.plot(sqrtSCross, crosSection)
ax.set_xlabel(r'$\sqrt{s}$ [GeV]')
ax.set_ylabel(r'$\sigma$ [pb]')
ax.set_yscale('log')
#ax.plot(ZMCross[0],ZMCross[1],label="Z mass")
#ax.plot(ZpMCross[0],ZpMCross[1],label="Z' mass")
#ax.legend(loc='best')
plt.savefig('ZCross.pdf')
#ax[1].text(x=1000,y=1770,s="Z'")
#ax[1].text(x=91,y=700,s="Z")

