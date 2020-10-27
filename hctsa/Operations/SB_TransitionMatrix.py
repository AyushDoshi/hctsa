import math

import numpy
import scipy.signal

from hctsa.Operations import CO_FirstZero
from hctsa.PeripheryFunctions import SB_CoarseGrain


def SB_TransitionMatrix(y, howtocg='quantile', numGroups=2, tau=1):
    """
    """
    if tau == 'ac':
        tau = CO_FirstZero(y)

    if tau > 1:
        y = scipy.signal.resample(y, math.ceil(len(y) / tau))

    N = len(y)

    yth = SB_CoarseGrain(y, howtocg, numGroups)

    if yth.shape[1] > yth.shape[0]:
        yth = yth.transpose()

    T = numpy.zeros((numGroups, numGroups))

    for i in range(0, numGroups):

        ri = (yth == i + 1)

        if sum(ri) == 0:

            T[i, :] = 0

        else:

            ri_next = numpy.append([False], ri[:-1])

            for j in range(numGroups):
                T[i, j] = numpy.sum((yth[ri_next] == j + 1))
    out = {}

    T /= N - 1

    if numGroups == 2:

        for i in range(2):

            for j in range(2):
                out['T' + str(i) + str(j)] = T[i, j]

    elif numGroups == 3:

        for i in range(3):

            for j in range(3):
                out['T' + str(i) + str(j)] = T[i, j]

    elif numGroups > 3:

        for i in range(numGroups):
            out['TD' + str(i)] = T[i, i]

    out['ondiag'] = numpy.sum(numpy.diag(T))

    out['stddiag'] = numpy.std(numpy.diag(T))

    out['symdiff'] = numpy.sum(numpy.sum(numpy.absolute(T - T.transpose())))

    out['symsumdiff'] = numpy.sum(numpy.sum(numpy.tril(T, -1)) - numpy.sum(numpy.triu(T, 1)))

    covT = numpy.cov(T.transpose())

    out['sumdiagcov'] = numpy.sum(numpy.diag(covT))

    eigT = numpy.linalg.eigvals(T)

    out['stdeig'] = numpy.std(eigT)

    out['maxeig'] = numpy.real(numpy.max(eigT))

    out['mineig'] = numpy.real(numpy.min(eigT))

    eigcovT = numpy.linalg.eigvals(covT)

    out['stdcoveig'] = numpy.std(eigcovT)

    out['maxcoveig'] = numpy.max(eigcovT)

    out['mincoveig'] = numpy.min(eigcovT)

    return out
