import numpy
import matplotlib
import matplotlib.pyplot as plt

from geomint import *

def main():
    # construct the Hamiltonian
    Hp = lambda p, q: p
    Hq = lambda p, q: numpy.sin(q)
    H = Hamiltonian(Hp, Hq, 1)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hold(True)

    # solve the initial value problem for the Hamiltonian
    # using the Stormer-Verlet algorithm for various t and
    # various p0
    q0 = 0.0
    for p0 in numpy.linspace(0.1, 2.0, 8):
        t = numpy.linspace(0, 6, 32)
        p, q = H.solve(p0, q0, t, solver=StormerVerlet)

        # plot the solution in the p-q plane
        ax.plot(p0, q0, 'ko', markersize=10)
        ax.plot(p, q, 'b')

    plt.show()


if __name__=='__main__':
    main()
