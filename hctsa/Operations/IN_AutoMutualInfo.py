import numpy

from hctsa.Operations import CO_FirstZero


def IN_AutoMutualInfo(y, timeDelay=1, estMethod='gaussian', extraParam=None):
    """
    """
    if extraParam is None:
        extraParam = []
    if isinstance(timeDelay, str):
        timeDelay = CO_FirstZero(y)

    N = len(y)

    if isinstance(timeDelay, list):

        numTimeDelays = len(timeDelay)

    else:

        numTimeDelays = 1

        timeDelay = [timeDelay]

    amis = []

    out = {}

    for k in range(numTimeDelays):

        y1 = y[0:N - timeDelay[k]]
        y2 = y[timeDelay[k]:N]

        if estMethod == 'gaussian':
            r = numpy.corrcoef(y1, y2)[1, 0]

            amis.append(-.5 * numpy.log(1 - r ** 2))

            out['Auto Mutual ' + str(timeDelay[k])] = -.5 * numpy.log(1 - r ** 2)

    return out
