import numpy
from scipy import stats


def EX_MovingThreshold(y, a=1, b=.1):
    """
    """
    if b < 0 or b > 1:
        print("b must be between 0 and 1")
        return None

    N = len(y)
    y = numpy.absolute(y)
    q = numpy.zeros(N)
    kicks = numpy.zeros(N)

    q[0] = 1

    for i in range(1, N):

        if y[i] > q[i - 1]:

            q[i] = (1 + a) * y[i]
            kicks[i] = q[i] - q[i - 1]

        else:

            q[i] = (1 - b) * q[i - 1]

    outDict = {'meanq': numpy.mean(q), 'medianq': numpy.median(q), 'iqrq': stats.iqr(q), 'maxq': numpy.max(q), 'minq': numpy.min(q),
               'stdq': numpy.std(q), 'meanqover': numpy.mean(q - y), 'pkick': numpy.sum(kicks) / N - 1}

    fkicks = numpy.argwhere(kicks > 0).flatten()
    Ikicks = numpy.diff(fkicks)
    outDict['stdkicks'] = numpy.std(Ikicks)
    outDict['meankickf'] = numpy.mean(Ikicks)
    outDict['mediankicksf'] = numpy.median(Ikicks)

    return outDict
