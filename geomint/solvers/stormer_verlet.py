import scipy
import scipy.optimize

from .solver import Solver

class StormerVerlet_Solver(Solver):
    def __repr__(self):
        return 'Stormer-Verlet Hamiltonian solver.'

    def step(self, H, pn, qn, h):
        # implicit half step in p
        f = lambda p: pn - (h/2)*H.Hq(p, qn) - p
        phalf = scipy.optimize.newton(f, pn)

        # implicit step in q
        g = lambda q: qn + (h/2)*(H.Hp(phalf, qn) + H.Hp(phalf, q)) - q
        qnp1 = scipy.optimize.newton(g, qn)

        # explicit half step in p
        pnp1 = phalf - (h/2)*H.Hq(phalf, qnp1)
        return pnp1, qnp1

StormerVerlet = StormerVerlet_Solver()
