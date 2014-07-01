import numpy

class Solver(object):
    r"""Abstract Hamiltonian solver object.

    Methods
    -------

    solve

    """
    def __init__(self):
        pass

    def __repr__(self):
        return 'Abstract Hamiltonian solver.'

    def step(self, H, pn, qn, h):
        raise NotImplementedError('Implement the single-step algorithm.')

    def solve(self, H, p0, q0, t):
        r"""Solve for p(t) and q(t) with the Hamiltonian H.

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


