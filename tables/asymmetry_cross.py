import numpy as np
import matplotlib.pyplot as plt

inFile = open("Zp_Asymmetry.txt",'r')
process = inFile.readline()
xaxis   = inFile.readline()
title   = inFile.readline()
inFile.close()

sqrtSAsym, Asymmetry = np.loadtxt('Zp_Asymmetry.txt',unpack=True,skiprows=3)
sqrtSCross, crosSection = np.loadtxt('Zp_cross.txt',unpack=True,skiprows=3)
ZMAsym  = [[91,91],[np.min(Asymmetry),np.max(Asymmetry)]]
ZMCross = [[91,91],[np.min(crosSection),np.max(crosSection)]]
ZpMAsym  = [[1000,1000],[np.min(Asymmetry),np.max(Asymmetry)]]
ZpMCross = [[1000,1000],[np.min(crosSection),np.max(crosSection)]]

fig, ax = plt.subplots(nrows=2,ncols=1)

ax[0].set_title(process)
ax[0].plot(sqrtSAsym, Asymmetry)
ax[0].plot(ZMAsym[0],ZMAsym[1],label="Z mass")
ax[0].plot(ZpMAsym[0],ZpMAsym[1],label="Z' mass")
ax[0].legend(loc='best')
ax[0].set_xlabel(r'$\sqrt{s}$ [GeV]')
ax[0].set_ylabel('Asymmetry')
#ax[0].text(x=91,y=0.6,s="Z")
#ax[0].text(x=1000,y=0.6,s="Z'")

ax[1].plot(sqrtSCross, crosSection)
ax[1].set_xlabel(r'$\sqrt{s}$ [GeV]')
ax[1].set_ylabel(r'Cross section [pb]')
ax[1].set_yscale('log')
ax[1].plot(ZMCross[0],ZMCross[1],label="Z mass")
ax[1].plot(ZpMCross[0],ZpMCross[1],label="Z' mass")
ax[1].legend(loc='best')
#ax[1].text(x=1000,y=1770,s="Z'")
#ax[1].text(x=91,y=700,s="Z")

plt.show()
