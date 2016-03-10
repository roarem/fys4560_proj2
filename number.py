import numpy as np

mTau = 1.777

def nEvents(s):
    a = 2/3*((4*np.pi)**4*s)*np.sqrt(1-4*(mTau**2/s))*(1+2*mTau**2/s)
    a = aa
    return a


print(nEvents(5))
print(nEvents(50))
print(nEvents(91))
print(nEvents(125))
