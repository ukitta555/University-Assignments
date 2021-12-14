from LongComparison import LongComparison
from LongNumber import LongNumber
import itertools
import functools

class SystemLongComparison:
    def __init__(self, comparisons):
        self.c = comparisons

    # using chinese remainder theorem
    def solve(self):
        self.normalize()
        list_m = [i.m for i in self.c]   # list of m_s
        list_b = [i.b for i in self.c]   # list of b's
        m = functools.reduce(lambda a, b: a * b, list_m)    # get a product of all modulos
        list_M = [m // n.m for n in self.c]  # get list of M_s
        # M_s = 1 (mod m_s) -> solve it, get all solutions (N_s) out of it
        list_Mi = [LongComparison(a, LongNumber('1'), m).solve()[0] for a, m in zip(list_M, list_m)]
        x = [a*b*c for a,b,c in zip(list_b, list_M, list_Mi)]  # b * M_s * M_i
        s = functools.reduce(lambda a, b: a + b, x)  # (b*m_s*m_i)_j1 + (b*m_s*m_i)_j2 + ....

        return s % m, m     # solution

    def normalize(self):
        new = []
        for c in self.c:    # for each comparison:
            b, m = c.solve()    # 1. solve it
            new.append(LongComparison(LongNumber('1'), b, m))  # 2. create new comparison with a = 1
        self.c = new # reassign system -> all comparisons look like x=b(mod m)
        self.coprime_modules()

    def coprime_modules(self):
        to_delete = []
        for i, j in itertools.combinations(self.c, 2):  # for each pair of comparisons
            new = i.combine(j) # combine i comparison with j
            if new: # if ok:
                self.c.append(new)