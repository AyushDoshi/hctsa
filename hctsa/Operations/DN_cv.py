# import warnings
# @numba.jit(nopython=True,parallel=True)
import numpy


def DN_cv(x, k=1):
    """
    """
    # if k % 1 != 0 or k < 0:
    #     warnings.warn("k should probably be positive int")
    if numpy.mean(x) == 0:
        return numpy.nan
    return (numpy.std(x) ** k) / (numpy.mean(x) ** k)
