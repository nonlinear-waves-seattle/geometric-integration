from solvers import SymplecticEuler

class Hamiltonian(object):
    def __init__(self, Hp, Hq, dim=None):
        self.Hp = Hp
        self.Hq = Hq

        if dim is None:
            raise ValueError('Specify dimension of p and q.')
        self._dim = dim

    def dim(self):
        return self._dim

    def solve(self, p0, q0, t, solver=SymplecticEuler):
        return solver.solve(self, p0, q0, t)
