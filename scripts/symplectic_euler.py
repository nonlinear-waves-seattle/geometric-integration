import numpy
import scipy
import scipy.optimize
import matplotlib
import matplotlib.pyplot as plt

from scipy.optimize import newton

def symplectic_euler_step(a, b, un, vn, h):
    # Implicit step: u(n+1) = u(n) + h*a(u(n+1),v(n))
    f = lambda u: un + h*a(u,vn) - u
    unp1 = newton(f,un)

    # Explicit step: v(n+1) = v(n) + h*b(u(n+1),v(n))
    vnp1 = vn + h*b(unp1,vn)
    return unp1, vnp1


def symplectic_euler(a, b, u0, v0, h=1.0, nsteps=10):
    """Solve the system :math:`u'=a(u,v), v'=b(u,v)` with symplectic Euler.

    Given a system

    .. math::

        u' = a(u,v), v' = b(u,v)

    with initial condition :math:`u_0,v_0` solve the system using the
    symplectic Euler method with step size ``h`` and ``nsteps`` number
    of iterations.

    The symplectic Euler method takes an implicit step in :math:`u` and
    an explicit step in :math:`v` on each iteration.

    .. math::

        u_{n+1} = u_n + h a(u_{n+1}, v_n) \\
        v_{n+1} = v_n + h b(u_{n+1}, v_n)

    Parameters
    ----------
    a,b : function
        The system of equations.
    u0,v0 : float
        The initial condition of the system.
    h : float
        Iteration step size.
    nsteps : int
        Number of iterations to perform.

    Returns
    -------
    numpy.array
        The solutions :math:`u_n,v_n` to the system for ``nterms``
        iterations with step size of ``h``.

    """
    sols = numpy.zeros((nsteps+1,2))
    sols[0,0] = u0
    sols[0,1] = v0
    for n in range(nsteps):
        un,vn = sols[n,:]
        unp1,vnp1 = symplectic_euler_step(a,b,h,un,vn)
        sols[n+1,:] = (unp1,vnp1)
    return sols



if __name__ == '__main__':
    # Example from Hairer, et. al. page 4 "Lotka-Volterra equations"
    def a(u,v):
        return u*(v-2)

    def b(u,v):
        return v*(1-u)

    h = 0.12
    u0 = 4
    v0 = 2
    nsteps = 125
    sols = symplectic_euler(a, b, h, u0, v0, nsteps)

    # now plot
    u = sols[:,0]
    v = sols[:,1]
    plt.hold(True)
    plt.plot(u,v,'b')
    plt.plot(u,v,'b.')
    plt.plot(u[0],v[0],'ko',markersize=10)
    plt.title('Lotka-Volterra Equation')
    plt.xlabel('$u$')
    plt.ylabel('$v$')
    plt.axis([0,7,0,9])
