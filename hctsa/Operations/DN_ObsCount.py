import numpy


def DN_ObsCount(y):
    """
    """
    return numpy.count_nonzero(~numpy.isnan(y))
