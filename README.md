geometric-integration
=====================

Implementations of ODE Solvers from Geometric Numerical Integration by
Harier, et. al.

Quickstart
----------

We solve the pendulum problem using the Stormer-Verlet method:

    import numpy
    import matplotlib
    import matplotlib.pyplot as plt

    from geomint import *

    # construct the Hamiltonian
    Hp = lambda p, q: p
    Hq = lambda p, q: numpy.sin(q)
    H = Hamiltonian(Hp, Hq, dim=1)

    # solve the initial value problem for the Hamiltonian
    # using the Stormer-Verlet algorithm for various t
    p0 = -1.7
    q0 = 0.0
    t = numpy.linspace(0, 10, 64)
    p, q = H.solve(p0, q0, t, solver=StormerVerlet)

    # plot the solution in the p-q plane
    plt.plot(p, q)
    plt.show()

Installation
------------

You can run the above code by executing it in the top-level directory
``geometric-integration``. You can also install ``geomint`` system-wide
by running:

    $ python setup.py build
    # python setup.py install

Authors
-------

* Ben Segal (BenSegal)
* Natalie Sheils (nsheils)
* Chris Swierczewski (cswiercz)
* Olga Tritchenko (otritch)

