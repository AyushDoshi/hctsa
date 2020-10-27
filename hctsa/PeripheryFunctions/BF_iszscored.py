import numpy


def BF_iszscored(x):
    """
    """
    numericThreshold = 2.2204E-16
    iszscored = ((numpy.absolute(numpy.mean(x)) < numericThreshold) & (numpy.absolute(numpy.std(x) - 1) < numericThreshold))
    return iszscored
