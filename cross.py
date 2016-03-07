import numpy as np
import matplotlib.pyplot as plt

def crossSection(sqrtS):
    s = sqrtS*sqrtS
    m = 1.78
    sigma = (2/3)*(1/s)*np.sqrt(1-4*m*m/s)*(1+2*m*m/s)
    return sigma

sqrtS = np.linspace(1.78*1.78*4,150,100)

cross = crossSection(sqrtS)

fig, ax = plt.subplots()
ax.plot(sqrtS, cross)
plt.show()

