import numpy
import scipy
import scipy.optimize
import matplotlib
import matplotlib.pyplot as plt

from scipy.optimize import newton

def stormer_verlet_step(Hp, Hq, pn, qn, h):
    r"""Take a single Stormer-Verlet step.

    Parameters
    ----------

    Returns
    -------
    """
    f = lambda p: pn - (h/2)*Hq(p, qn) - p
    phalf = newton(f, pn)

    g = lambda q: qn + (h/2)*(Hp(phalf, qn) + Hp(phalf, q)) - q
    qnp1 = newton(g, qn)

    pnp1 = phalf - (h/2)*Hq(phalf, qnp1)
    return pnp1, qnp1


def _stormer_verlet_manual(Hp, Hq, p0, q0, h=1.0, nsteps=10, step_pref='p'):
    sols = numpy.zeros((nsteps+1,2))
    sols[0,0] = p0
    sols[0,1] = q0
    for n in range(nsteps):
        pn,qn = sols[n,:]
        pnp1,qnp1 = stormer_verlet_step(Hp,Hq,pn,qn,h)
        sols[n+1,:] = (pnp1,qnp1)
    return sols


def _stormer_verlet_euler(*args, **kwds):
    raise ImplementationError('Not implemented!')


def stormer_verlet(Hp, Hq, p0, q0, h=1.0, nsteps=10, method='manual'):
    r"""Stormer-Verlet Method.

    Solve a system of the form

    .. math::

        \dot{p} = -H_q(p,q) \\
        \dot{q} = H_p(p,q)

    Where :math:`H` is a Hamiltonian.

    """
    if method == 'manual':
        return _stormer_verlet_manual(Hp, Hq, p0, q0, h=h, nsteps=nsteps)
    elif method == 'euler':
        return _stormer_verlet_euler(Hp, Hq, p0, q0, h=h, nsteps=nstep)
    else:
        raise ValueError('Not a valid method.')


if __name__ == '__main__':
    # Example from Hairer, et. al. page 6 "Pendulum Problem & Stormer-Verlet"
    def Hp(p, q):
        return p

    def Hq(p, q):
        return numpy.sin(q)

    h = 0.1
    p0 = 0
    q0 = 2.0
    nsteps = 100
    sols = stormer_verlet(Hp, Hq, p0, q0, h=h, nsteps=nsteps)

    # now plot
    p = sols[:,0]
    q = sols[:,1]
    plt.hold(True)
    plt.plot(p, q, 'b')
    plt.plot(p, q, 'b.')
    plt.plot(p[0], q[0], 'ko', markersize=10)
    plt.title('Pendulum Problem')
    plt.xlabel('$p$')
    plt.ylabel('$q$')

    h = 0.1
    p0 = 0
    q0 = 2.5
    nsteps = 100
    sols = stormer_verlet(Hp, Hq, p0, q0, h=h, nsteps=nsteps)

    # now plot
    p = sols[:,0]
    q = sols[:,1]
    plt.hold(True)
    plt.plot(p, q, 'b')
    plt.plot(p, q, 'b.')
    plt.plot(p[0], q[0], 'ko', markersize=10)

    h = 0.1
    p0 = -2.0
    q0 = 0
    nsteps = 100
    sols = stormer_verlet(Hp, Hq, p0, q0, h=h, nsteps=nsteps)

    # now plot
    p = sols[:,0]
    q = sols[:,1]
    plt.hold(True)
    plt.plot(p, q, 'b')
    plt.plot(p, q, 'b.')
    plt.plot(p[0], q[0], 'ko', markersize=10)


    plt.show()
