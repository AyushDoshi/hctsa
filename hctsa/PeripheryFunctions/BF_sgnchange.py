import numpy


def BF_sgnchange(y, doFind=0):
    """
    """
    if doFind == 0:
        return numpy.multiply(y[1:], y[0:len(y) - 1]) < 0
    indexs = numpy.where((numpy.multiply(y[1:], y[0:len(y) - 1]) < 0))
    return indexs
