import numpy
from scipy import stats

from hctsa.Operations import CO_AutoCorr


def SY_LocalGlobal(y, subsetHow='l', n=''):
    """
    """
    if subsetHow == 'p' and n == '':

        n = .1

    elif n == '':

        n = 100

    N = len(y)

    if subsetHow == 'l':

        r = range(0, min(n, N))

    elif subsetHow == 'p':

        if n > 1:
            n = .1

        r = range(0, round(N * n))

    elif subsetHow == 'unicg':

        r = numpy.round(numpy.arange(0, N, n)).astype(int)

    elif subsetHow == 'randcg':

        r = numpy.random.randint(N, size=n)

    if len(r) < 5:
        out = numpy.nan
        return out

    out = {'absmean': numpy.absolute(numpy.mean(y[r])), 'std': numpy.std(y[r], ddof=1), 'median': numpy.median(y[r]),
           'iqr': numpy.absolute((1 - stats.iqr(y[r]) / stats.iqr(y)))}

    if stats.skew(y) == 0:

        out['skew'] = numpy.nan

    else:

        out['skew'] = numpy.absolute(1 - stats.skew(y[r]) / stats.skew(y))

    out['kurtosis'] = numpy.absolute(1 - stats.kurtosis(y[r], fisher=False) / stats.kurtosis(y, fisher=False))

    out['ac1'] = numpy.absolute(1 - CO_AutoCorr(y[r]) / CO_AutoCorr(y))

    return out
