import numpy

from hctsa.Operations import CO_glscf


def CO_fzcglscf(y, alpha, beta, maxtau='empty'):
    """
    """
    N = len(y)

    if maxtau == 'empty':
        maxtau = N

    glscfs = numpy.zeros(maxtau)

    for i in range(maxtau - 1):

        tau = i + 1

        glscfs[i] = CO_glscf(y, alpha, beta, tau)

        if i > 0 > glscfs[i] * glscfs[i - 1]:
            out = i + glscfs[i] / (glscfs[i] - glscfs[i - 1])

            return out

    return maxtau
