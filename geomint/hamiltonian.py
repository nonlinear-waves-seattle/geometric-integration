from solvers import SymplecticEuler

class Hamiltonian(object):
    r"""A Hamiltonian system.

    A Hamiltonian system defined by the system of equations

    .. math::

        \dot{p}(t) = - H_q(p, q), \\
        \dot{q}(t) = H_p(p, q).

    Construct a Hamiltonian object by providing the right-hand side
    functions :math:`H_p,H_q` and the dimension of the varaibles `p` and
    `q`.

    Attributes
    ----------
    Hp, Hq : functions
        Python functions defining the partial derivatives of the
        Hamiltonian.

    Methods
    -------
    solve

    Examples
    --------
    We construct the Hamiltonian system for the pendulum problem::

        >> from geomint import *
        >> import numpy
        >> Hp = lambda p,q: p
        >> Hq = lambda p,q: numpy.sin(q)
        >> H = Hamiltonian(Hp, Hq, 1)

    Contents
    --------
    """
    def __init__(self, Hp, Hq, dim=None):
        self.Hp = Hp
        self.Hq = Hq

        if dim is None:
            raise ValueError('Specify dimension of p and q.')
        self._dim = dim

    def dim(self):
        r"""Returns the dimension of the system.

        Returns
        -------
        int
        """
        return self._dim

    def solve(self, p0, q0, t, solver=SymplecticEuler):
        r"""Solve the initial value problem.

        Solve the initial value problem at times `t` for initial
        conditions `p0` and `q0` using the provided Solver.

        Parameters
        ----------
        p0, q0 : array
            The initial values.
        t : array
            The times at which to compute a solution.
        solver : Solver
            (default: SymplecticEuler)

        Returns
        -------
        array, array
            Two arrays representing the values of `p` and `q` at the
            times `t`.

        """
        return solver.solve(self, p0, q0, t)
