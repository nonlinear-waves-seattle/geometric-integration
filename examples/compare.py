import numpy
import matplotlib
import matplotlib.pyplot as plt

from geomint import *

def main():
    # comparison of different integrators on the pendulum problem: plot
    # the solutions for various initial conditions and various solvers

    # construct the Hamiltonian
    Hp = lambda p, q: p
    Hq = lambda p, q: numpy.sin(q)
    H = Hamiltonian(Hp, Hq, 1)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.hold(True)

    # construct a list of various initial conditions _and_ solvers
    p0s = numpy.linspace(0.1, 2.0, 5)
    solvers = [SymplecticEuler, StormerVerlet]
    colors = ['b', 'g']
    N = len(solvers)

    print 'Computing...'
    for p0 in p0s:
        q0 = 0.0
        t = numpy.linspace(0, 6, 32)

        # plot the starting point
        ax.plot(p0, q0, 'ko', markersize=5)
        print '\tp0 = %f\tq0 = %f'%(p0,q0)

        # solve for the given initial condition using different solvers
        # (and colors to plot)
        for solver, color in zip(solvers, colors):
            p, q = H.solve(p0, q0, t, solver=solver)
            ax.plot(p, q, color=color)

    print 'Plotting...'
    ax.set_xlabel('p')
    ax.set_ylabel('q')
    plt.show()


if __name__=='__main__':
    main()
