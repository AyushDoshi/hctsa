import numpy
from scipy import stats


def DN_Mode(y):
    """
    """
    # y must be numpy array
    if not isinstance(y, numpy.ndarray):
        y = numpy.asarray(y)
    return float(stats.mode(y).mode)
