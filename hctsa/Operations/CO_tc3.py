import numpy

from hctsa.Operations import CO_FirstZero, CO_FirstMin


def CO_tc3(y, tau='ac'):
    """
    """
    if tau == 'ac':

        tau = CO_FirstZero(y)

    else:

        tau = CO_FirstMin(y, 'mi')

    N = len(y)

    yn = y[0:N - 2 * tau]
    yn1 = y[tau:N - tau]
    yn2 = y[tau * 2:N]

    raw = numpy.mean(numpy.multiply(numpy.multiply(yn, yn1), yn2)) / (numpy.absolute(numpy.mean(numpy.multiply(yn, yn1))) ** (3 / 2))

    outDict = {'raw': raw, 'abs': numpy.absolute(raw), 'num': numpy.mean(numpy.multiply(yn, numpy.multiply(yn1, yn2)))}

    outDict['absnum'] = numpy.absolute(outDict['num'])

    outDict['denom'] = numpy.absolute(numpy.mean(numpy.multiply(yn, yn1))) ** (3 / 2)

    return outDict
