import numpy as np
import matplotlib.pyplot as plt

def crossSection(sqrtS):
    s = sqrtS*sqrtS
    m = 1.78
    sigma = (2/3)*(1/s)*np.sqrt(1-4*m*m/s)*(1+2*m*m/s)
    return sigma

sqrtS = np.linspace(1.78*1.78*4,150,100)

cross = crossSection(sqrtS)*0.3894*1e-3

fig, ax = plt.subplots()
ax.plot(sqrtS, cross)
ax.set_ylabel(r"$\sigma [b]$")
ax.set_xlabel(r"s [$GeV$]")
ax.ticklabel_format(style='sci', axis='y')
ax.yaxis.major.formatter.set_powerlimits((0,0)) 
plt.savefig('QEDcross.pdf')
