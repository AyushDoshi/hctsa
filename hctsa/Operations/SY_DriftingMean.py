import math

import numpy


def SY_DriftingMean(y, howl='num', l=''):
    """
    """
    N = len(y)

    if howl == 'num':

        if l != '':
            l = math.floor(N / l)

    if l == '':

        if howl == 'num':

            l = 5

        elif howl == 'fix':

            l = 200

    if l == 0 or N < l:
        return

    numFits = math.floor(N / l)
    z = numpy.zeros((l, numFits))

    for i in range(0, numFits):
        z[:, i] = y[i * l:(i + 1) * l]

    zm = numpy.mean(z, axis=0)
    zv = numpy.var(z, axis=0, ddof=1)

    meanvar = numpy.mean(zv)
    maxmean = numpy.max(zm)
    minmean = numpy.min(zm)
    meanmean = numpy.mean(zm)

    outDict = {'max': maxmean / meanvar, 'min': minmean / meanvar, 'mean': meanmean / meanvar}

    outDict['meanmaxmin'] = (outDict['max'] + outDict['min']) / 2
    outDict['meanabsmaxmin'] = (numpy.absolute(outDict['max']) + numpy.absolute(outDict['min'])) / 2

    return outDict
