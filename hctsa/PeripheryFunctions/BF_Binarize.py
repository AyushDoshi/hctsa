import numpy


def BF_Binarize(y, binarizeHow='diff'):
    """
    """
    if binarizeHow == 'diff':
        yBin = stepBinary(numpy.diff(y))

    if binarizeHow == 'mean':
        yBin = stepBinary(y - numpy.mean(y))

    if binarizeHow == 'median':
        yBin = stepBinary(y - numpy.median(y))

    if binarizeHow == 'iqr':
        iqr = numpy.quantile(y, [.25, .75])

        iniqr = numpy.logical_and(y > iqr[0], y < iqr[1])

        yBin = numpy.zeros(len(y))

        yBin[iniqr] = 1

    return yBin


def stepBinary(X):
    """
    """
    Y = numpy.zeros(len(X))

    Y[X > 0] = 1

    return Y
