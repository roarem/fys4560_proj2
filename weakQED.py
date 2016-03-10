import sympy as s
from sympy.matrices import Matrix
t = s.symbols('t')
g0  =   Matrix([[1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,-1]])
g1  =   Matrix([[0,0,0,1],[0,0,1,0],[0,-1,0,0],[-1,0,0,0]])
g2  =   Matrix([[0,0,0,-s.I],[0,0,s.I,0],[0,s.I,0,0],[-s.I,0,0,0]])
g3  =   Matrix([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
uup =   Matrix([1,0,1,0])
udp =   Matrix([0,1,0,-1])
vup =   Matrix([1,0,-1,0])
vdp =   Matrix([0,-1,0,-1])
uuk =   Matrix([s.cos(t),s.sin(t),s.cos(t),s.sin(t)])
udk =   Matrix([-s.sin(t),s.cos(t),s.sin(t),-s.cos(t)])
vuk =   Matrix([s.cos(t),s.sin(t),-s.cos(t),-s.sin(t)])
vdk =   Matrix([s.sin(t),-s.cos(t),s.sin(t),-s.cos(t)])


'''
print("uup vdp")
print(20*'-')
print((uup.T*g0*g0*vdp)[0,0],end=" | ")
print((uup.T*g0*g1*vdp)[0,0],end=" | ")
print((uup.T*g0*g2*vdp)[0,0],end=" | ")
print((uup.T*g0*g3*vdp)[0,0],end="\n")
print(20*'-')
print("udp vup")
print(20*'-')
print((udp.T*g0*g0*vup)[0,0],end=" | ")
print((udp.T*g0*g1*vup)[0,0],end=" | ")
print((udp.T*g0*g2*vup)[0,0],end=" | ")
print((udp.T*g0*g3*vup)[0,0],end="\n")
print(20*'-')
print("vup udp")
print(20*'-')
print((vup.T*g0*g0*udp)[0,0],end=" | ")
print((vup.T*g0*g1*udp)[0,0],end=" | ")
print((vup.T*g0*g2*udp)[0,0],end=" | ")
print((vup.T*g0*g3*udp)[0,0],end="\n")
print(20*'-')
print("vdp uup")
print(20*'-')
print((vdp.T*g0*g0*uup)[0,0],end=" | ")
print((vdp.T*g0*g1*uup)[0,0],end=" | ")
print((vdp.T*g0*g2*uup)[0,0],end=" | ")
print((vdp.T*g0*g3*uup)[0,0],end="\n")
print(20*'-')
print("uuk vdk")
print(20*'-')
print((uuk.T*g0*g0*vdk)[0,0],end=" | ")
print((uuk.T*g0*g1*vdk)[0,0],end=" | ")
print((uuk.T*g0*g2*vdk)[0,0],end=" | ")
print((uuk.T*g0*g3*vdk)[0,0],end="\n")
print(20*'-')
print("udk vuk")
print(20*'-')
print((udk.T*g0*g0*vuk)[0,0],end=" | ")
print((udk.T*g0*g1*vuk)[0,0],end=" | ")
print((udk.T*g0*g2*vuk)[0,0],end=" | ")
print((udk.T*g0*g3*vuk)[0,0],end="\n")
print(20*'-')
print("vuk udk")
print(20*'-')
print((vuk.T*g0*g0*udk)[0,0],end=" | ")
print((vuk.T*g0*g1*udk)[0,0],end=" | ")
print((vuk.T*g0*g2*udk)[0,0],end=" | ")
print((vuk.T*g0*g3*udk)[0,0],end="\n")
print(20*'-')
print("vdk uuk")
print(20*'-')
print((vdk.T*g0*g0*uuk)[0,0],end=" | ")
print((vdk.T*g0*g1*uuk)[0,0],end=" | ")
print((vdk.T*g0*g2*uuk)[0,0],end=" | ")
print((vdk.T*g0*g3*uuk)[0,0],end="\n")
'''
'''
uup1 = Matrix([(uup.T*g0*g0*vdp)[0,0],(uup.T*g0*g1*vdp)[0,0],(uup.T*g0*g2*vdp)[0,0],(uup.T*g0*g3*vdp)[0,0]])

udp1 = Matrix([(udp.T*g0*g0*vup)[0,0],(udp.T*g0*g1*vup)[0,0],(udp.T*g0*g2*vup)[0,0],(udp.T*g0*g3*vup)[0,0]])

vup1 = Matrix([(vup.T*g0*g0*udp)[0,0],(vup.T*g0*g1*udp)[0,0],(vup.T*g0*g2*udp)[0,0],(vup.T*g0*g3*udp)[0,0]])

vdp1 = Matrix([(vdp.T*g0*g0*uup)[0,0],(vdp.T*g0*g1*uup)[0,0],(vdp.T*g0*g2*uup)[0,0],(vdp.T*g0*g3*uup)[0,0]])

uuk1 = Matrix([(uuk.T*g0*g0*vdk)[0,0],(uuk.T*g0*g1*vdk)[0,0],(uuk.T*g0*g2*vdk)[0,0],(uuk.T*g0*g3*vdk)[0,0]])

udk1 = Matrix([(udk.T*g0*g0*vuk)[0,0],(udk.T*g0*g1*vuk)[0,0],(udk.T*g0*g2*vuk)[0,0],(udk.T*g0*g3*vuk)[0,0]])

vuk1 = Matrix([(vuk.T*g0*g0*udk)[0,0],(vuk.T*g0*g1*udk)[0,0],(vuk.T*g0*g2*udk)[0,0],(vuk.T*g0*g3*udk)[0,0]])

vdk1 = Matrix([(vdk.T*g0*g0*uuk)[0,0],(vdk.T*g0*g1*uuk)[0,0],(vdk.T*g0*g2*uuk)[0,0],(vdk.T*g0*g3*uuk)[0,0]])

print(s.simplify(((vdk1.T*uup1)*(vdp1.T*uuk))[0,0]))
'''