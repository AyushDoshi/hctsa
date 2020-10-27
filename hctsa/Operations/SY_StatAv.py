import math

import numpy


def SY_StatAv(y, whatType='seg', n=5):
    """
    """
    N = len(y)

    if whatType == 'seg':

        M = numpy.zeros(n)
        p = math.floor(N / n)

        for j in range(1, n + 1):
            M[j - 1] = numpy.mean(y[p * (j - 1):p * j])

    elif whatType == 'len':

        if N > 2 * n:

            pn = math.floor(N / n)
            M = numpy.zeros(pn)

            for j in range(1, pn + 1):
                M[j - 1] = numpy.mean(y[(j - 1) * n:j * n])

        else:

            return

    s = numpy.std(y, ddof=1)
    sdav = numpy.std(M, ddof=1)

    out = sdav / s

    return out
