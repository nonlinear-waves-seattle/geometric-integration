import numpy
import matplotlib
import matplotlib.pyplot as plt

from geomint import *

# construct the Hamiltonian
Hp = lambda p, q: p
Hq = lambda p, q: numpy.sin(q)
H = Hamiltonian(Hp, Hq, 1)

# solve the initial value problem for the Hamiltonian
# using the Stormer-Verlet algorithm for various t
p0 = -1.7
q0 = 0.0
t = numpy.linspace(0, 10, 64)
p, q = H.solve(p0, q0, t, solver=StormerVerlet)

# plot the solution in the p-q plane
plt.plot(p, q)
plt.show()
