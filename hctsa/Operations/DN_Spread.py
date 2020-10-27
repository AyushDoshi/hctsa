# @numba.jit(nopython=True,parallel=True)
import numpy
from scipy import stats


def DN_Spread(y, spreadMeasure='std'):
    """
    """
    if spreadMeasure == 'std':
        return numpy.std(y)
    elif spreadMeasure == 'iqr':
        return stats.iqr(y)
    elif spreadMeasure == 'mad':
        return mad(y)
    elif spreadMeasure == 'mead':
        return mead(y)  # stats.median_absolute_deviation(y)
    else:
        raise Exception('spreadMeasure must be one of std, iqr, mad or mead')


def mad(data, axis=None):
    """
    """
    return numpy.mean(numpy.absolute(data - numpy.mean(data, axis)), axis)


def mead(data, axis=None):
    """
    """
    return numpy.median(numpy.absolute(data - numpy.median(data, axis)), axis)
