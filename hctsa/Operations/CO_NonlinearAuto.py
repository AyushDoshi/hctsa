import numpy


def CO_NonlinearAutocorr(y, taus, doAbs='empty'):
    """
    """
    if doAbs == 'empty':

        if len(taus) % 2 == 1:

            doAbs = 0

        else:

            doAbs = 1

    N = len(y)
    tmax = numpy.max(taus)

    nlac = y[tmax:N]

    for i in taus:
        nlac = numpy.multiply(nlac, y[tmax - i:N - i])

    if doAbs:

        return numpy.mean(numpy.absolute(nlac))

    else:

        return numpy.mean(nlac)
