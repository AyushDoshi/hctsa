import numpy

from hctsa.Operations import CO_FirstZero


def CO_glscf(y, alpha=1.0, beta=1.0, tau=''):
    """
    """
    if tau == '':
        tau = CO_FirstZero(y)

    N = len(y)

    beta = float(beta)
    alpha = float(alpha)

    y1 = numpy.absolute(y[0:N - tau])

    y2 = numpy.absolute(y[tau:N])

    top = numpy.mean(numpy.multiply(numpy.power(y1, alpha), numpy.power(y2, beta))) - numpy.mean(numpy.power(y1, alpha)) * numpy.mean(
        numpy.power(y2, beta))

    bot = numpy.sqrt(numpy.mean(numpy.power(y1, 2 * alpha)) - numpy.mean(numpy.power(y1, alpha)) ** 2) * numpy.sqrt(
        numpy.mean(numpy.power(y2, 2 * beta)) - numpy.mean(numpy.power(y2, beta)) ** 2)

    if bot == 0:
        return numpy.inf

    glscf = top / bot

    return glscf
