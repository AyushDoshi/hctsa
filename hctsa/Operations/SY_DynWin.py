import math

import numpy
from scipy import stats

from hctsa.Operations import CO_FirstZero, CO_AutoCorr


def SY_DynWin(y, maxnseg=10):
    """
    """
    nsegr = numpy.arange(2, maxnseg + 1)

    nmov = 1

    numFeatures = 9

    fs = numpy.zeros((len(nsegr), numFeatures))

    taug = CO_FirstZero(y)

    for i in range(len(nsegr)):

        nseg = nsegr[i]

        wlen = math.floor(len(y) / nseg)

        inc = math.floor(wlen / nmov)

        if inc == 0:
            inc = 1

        numSteps = math.floor((len(y) - wlen) / inc) + 1

        qs = numpy.zeros((numSteps, numFeatures))

        for j in range(numSteps):
            ysub = y[j * inc:j * inc + wlen]

            taul = CO_FirstZero(ysub)

            qs[j, 0] = numpy.mean(ysub)

            qs[j, 1] = numpy.std(ysub, ddof=1)

            qs[j, 2] = stats.skew(ysub)

            qs[j, 3] = stats.kurtosis(ysub)

            qs[j, 4] = CO_AutoCorr(ysub)

            qs[j, 5] = CO_AutoCorr(ysub, 2)

            qs[j, 6] = CO_AutoCorr(ysub, taug)

            qs[j, 7] = CO_AutoCorr(ysub, taul)

            qs[j, 8] = taul

        fs[i, :] = numpy.std(qs, axis=0, ddof=1)

    fs = numpy.std(fs, axis=0, ddof=1)

    outDict = {'stdmean': fs[0], 'stdstd': fs[1], 'stdskew': fs[2], 'stdkurt': fs[3], 'stdac1': fs[4], 'stdac2': fs[5],
               'stdactaug': fs[6], 'stdactaul': fs[7], 'stdtaul': fs[8]}

    return outDict
