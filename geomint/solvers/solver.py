import numpy

class Solver(object):
    r"""Abstract Hamiltonian solver object.

    Implementations of Hamiltonian solvers should inherit from this
    object and define the method :py:meth:`step`. ``step`` defines how
    the implemented method performs a single time step of size `h`.

    Attributes
    ----------
    None

    Methods
    -------
    solve

    Contents
    --------
    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'Abstract Hamiltonian solver.'

    def step(self, H, pn, qn, h):
        r"""Perform a single time step of the solver.

        Parameters
        ----------
        H : Hamiltonian
        pn, qn : arrays
            The Hamiltonian and a solution at some time.
        h : double
            The size of the time step to take.

        Returns
        -------
        array, array
            The values of `p` and `q` after a step of size `h`.

        .. note::

            This method must be implemented in subclasses.

        """
        raise NotImplementedError('Implement the single-step algorithm.')

    def solve(self, H, p0, q0, t):
        r"""Solve for `p(t)` and `q(t)` with the Hamiltonian `H`.

        Parameters
        ----------
        H : Hamiltonian
        p0 : array
        q0 : array
            The initial condition at time ``t0 = t[0]``.
        t : double or array
            The times at which to compute `p(t)` and `q(t)`.

        Returns
        -------
        arrays
            Return the arrays, :math:`p(t), q(t)` for the given `t`.

        """
        t = numpy.array(t)
        N = len(t)
        d = H.dim()

        # initialize the solution arrays
        p = numpy.zeros((N,d))
        q = numpy.zeros((N,d))
        p[0,:] = p0
        q[0,:] = q0

        # step for each time appearing in the array
        for n in range(1,N):
            h = t[n] - t[n-1]
            p[n], q[n] = self.step(H, p[n-1], q[n-1], h)
        return p, q


