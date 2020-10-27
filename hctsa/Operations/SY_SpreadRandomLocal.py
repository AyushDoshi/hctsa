import numpy
from scipy import stats

from hctsa.Operations import CO_FirstZero, CO_AutoCorr


def SY_SpreadRandomLocal(y, l=100, numSegs=25, randomSeed=0):
    """
    """
    if isinstance(l, str):
        taug = CO_FirstZero(y)

        if l == 'ac2':
            l = 2 * taug
        else:
            l = 5 * taug

    N = len(y)

    if l > .9 * N:
        # print('Time series too short for given l')
        return numpy.nan

    numFeat = 8

    qs = numpy.zeros((numSegs, numFeat))

    for j in range(numSegs):
        ist = numpy.random.randint(N - l)
        ifh = ist + l

        ysub = y[ist:ifh]

        taul = CO_FirstZero(ysub)

        qs[j, 0] = numpy.mean(ysub)

        qs[j, 1] = numpy.std(ysub)

        qs[j, 2] = stats.skew(ysub)

        qs[j, 3] = stats.kurtosis(ysub)

        # entropyDict = EN_SampEn(ysub,1,.15)

        # qs[j,4] = entropyDict['Quadratic Entropy']

        qs[j, 5] = CO_AutoCorr(ysub)

        qs[j, 6] = CO_AutoCorr(ysub, 2)

        qs[j, 7] = taul

    fs = numpy.zeros((numFeat, 2))

    fs[:, 0] = numpy.nanmean(qs, axis=0)

    fs[:, 1] = numpy.nanstd(qs, axis=0)

    out = {'meanmean': fs[0, 0], 'meanstd': fs[1, 0], 'meanskew': fs[2, 0], 'meankurt': fs[3, 0], 'meanac1': fs[5, 0],
           'meanac2': fs[6, 0], 'meantaul': fs[7, 0], 'stdmean': fs[0, 1], 'stdstd': fs[1, 1], 'stdskew': fs[2, 1],
           'stdkurt': fs[3, 1], 'stdac1': fs[5, 1], 'stdac2': fs[6, 1], 'stdtaul': fs[7, 1]}

    # out['meansampEn'] = fs[4,0]

    # out['stdsampEn'] = fs[4,1]

    return out
