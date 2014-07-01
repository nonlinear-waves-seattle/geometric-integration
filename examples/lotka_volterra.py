import numpy
import matplotlib
import matplotlib.pyplot as plt

from geomint import *

def main():
    # Example from Hairer, et. al. page 4 "Lotka-Volterra equations"
    # construct the Hamiltonian
    Hp = lambda p, q: p*(q-2)
    Hq = lambda p, q: q*(p-1)
    H = Hamiltonian(Hp, Hq, 1)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hold(True)

    # solve the initial value problem for the Hamiltonian using the
    # (default) Symplectic Euler algorithm for various t and various p0
    p0s = -numpy.arange(0.5, 4.0, 0.5)
    for p0 in p0s:
        q0 = 2*p0
        t = numpy.linspace(0, 6, 128)
        p, q = H.solve(p0, q0, t)

        # plot the solution in the p-q plane
        ax.plot(p0, q0, 'ko', markersize=10)
        ax.plot(p, q, 'b')

    plt.show()


if __name__=='__main__':
    main()
