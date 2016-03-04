geometric-integration
=====================

Implementations of ODE Solvers from Geometric Numerical Integration by
Harier, et. al.

Quickstart
----------

We solve the pendulum problem using the Stormer-Verlet method:

```python
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
```

Installation
------------

You can run the above code by executing it in the top-level directory
``geometric-integration``. You can also install ``geomint`` system-wide
by running:

    $ python setup.py build
    # python setup.py install

Examples
--------

Run the examples from the top-level directory ``geometric-integration``
like so:

    $ python examples/pendulum.py
    
Adding a New Solver
-------------------

It's easy to create a new Hamiltonian solver as long as you can implement the single-step function.

1. Create a new Python module ``mysolver.py`` in the ``geomint/solvers/`` directory.
2. Inside the file, create a new subclass of the `Solver` class and an instance of it like so:

    ```python
    from .solver import Solver
    class MySolver_Solver(Solver):
        def step(self, H, pn, qn, h):
            # code to compute the next iterate, pnp1 and qnp1, using
            # the Hamiltonian H, current values pn and qn, and step
            # size h
            return pnp1, qnp1
    MySolver = MySolver_Solver()
    ```
    
3. "Register" your solver with geomint by adding the following line to ``geomint/solvers/__init__.py``:

    ```python
    from .mysolver import MySolver
    ```
    
4. That's it! Your new solver is now accessible from the rest of the software.

Authors
-------

* Ben Segal (BenSegal)
* Natalie Sheils (nsheils)
* Chris Swierczewski (cswiercz)
* Olga Tritchenko (otritch)

