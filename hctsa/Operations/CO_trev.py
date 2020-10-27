import numpy

from hctsa.Operations import CO_FirstZero, CO_FirstMin


def CO_trev(y, tau='ac'):
    """
    """
    if tau == 'ac':

        tau = CO_FirstZero(y)

    else:

        tau = CO_FirstMin(y, 'mi')

    N = len(y)

    yn = y[0:N - tau]
    yn1 = y[tau:N]

    raw = numpy.mean(numpy.power(yn1 - yn, 3)) / numpy.mean(numpy.power(yn1 - yn, 2)) ** (3 / 2)

    outDict = {'raw': raw, 'abs': numpy.absolute(raw), 'num': numpy.mean(numpy.power(yn1 - yn, 3))}

    outDict['absnum'] = numpy.absolute(outDict['num'])

    outDict['denom'] = numpy.mean(numpy.power(yn1 - yn, 2)) ** (3 / 2)

    return outDict
