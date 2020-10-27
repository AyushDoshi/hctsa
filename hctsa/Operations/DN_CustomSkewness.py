# @numba.jit(nopython=True,parallel=True)
import numpy


def DN_CustomSkewness(y, whatSkew='pearson'):
    """
    """
    if whatSkew == 'pearson':
        if numpy.std(y) != 0:
            return (3 * numpy.mean(y) - numpy.median(y)) / numpy.std(y)
        else:
            return 0
    elif whatSkew == 'bowley':
        qs = numpy.quantile(y, [.25, .5, .75])
        if numpy.std(y) != 0:
            return (qs[2] + qs[0] - 2 * qs[1]) / (qs[2] - qs[0])
        else:
            return 0

    else:
        raise Exception('whatSkew must be either pearson or bowley.')
