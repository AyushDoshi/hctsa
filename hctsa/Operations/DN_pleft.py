# @numba.jit(nopython=True,parallel=True)
# oddly this function slows down with numba
import numpy


def DN_pleft(y, th=.1):
    """
    """
    p = numpy.quantile(numpy.absolute(y - numpy.mean(y)), 1 - th)

    return p / numpy.std(y, ddof=1)
