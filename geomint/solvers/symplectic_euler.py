import scipy
import scipy.optimize

from .solver import Solver

class SymplecticEuler_Solver(Solver):
    def __repr__(self):
        return 'Symplectic Euler Hamiltonian solver.'

    def step(self, H, pn, qn, h):
        # implicit step in p
        f = lambda p: pn - h*H.Hq(p, qn) - p
        pnp1 = scipy.optimize.newton(f, pn)

        # explicit step in q
        qnp1 = qn + h*H.Hp(pnp1, qn)
        return pnp1, qnp1


SymplecticEuler = SymplecticEuler_Solver()
