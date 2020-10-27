# @numba.jit(nopython=True,parallel=True)
import numpy
from scipy import stats


def DN_Withinp(x, p=1, meanOrMedian='mean'):
    """
    """
    N = len(x)

    if meanOrMedian == 'mean':
        mu = numpy.mean(x)
        sig = numpy.std(x)
    elif meanOrMedian == 'median':
        mu = numpy.median(x)
        sig = 1.35 * stats.iqr(x)
    else:
        raise Exception('Unknown meanOrMedian should be mean or median')
    return numpy.sum((x >= mu - p * sig) & (x <= mu + p * sig)) / N
