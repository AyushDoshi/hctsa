import numpy

from hctsa.Operations import CO_AutoCorr, CO_FirstZero


def PH_ForcePotential(y, whatPotential='dblwell', params=None):
    """
    """
    if params is None:
        params = []
    if not params:

        if whatPotential == 'dblwell':

            params = [2, .1, .1]

        elif whatPotential == 'sine':

            params = [1, 1, 1]

        else:

            print('Unreconginzed Potential')
            return

    N = len(y)

    if len(params) < 3:
        print('3 Parameters required')
        return

    alpha = params[0]
    kappa = params[1]
    deltat = params[2]

    if whatPotential == 'dblwell':
        def F(x):
            """
            """
            return - numpy.power(x, 3) + alpha ** 2 * x

        def V(x):
            """
            """
            return numpy.power(x, 4) / 4 - alpha ** 2 * numpy.power(x, 2) / 2

    if whatPotential == 'sine':
        def F(x):
            """
            """
            return numpy.sin(x / alpha) / alpha

        def V(x):
            """
            """
            return - numpy.cos(x / alpha)

    x = numpy.zeros(N)
    v = numpy.zeros(N)

    for i in range(1, N):
        x[i] = x[i - 1] + v[i - 1] * deltat + (F(x[i - 1]) + y[i - 1] - kappa * v[i - 1]) * deltat ** 2
        v[i] = v[i - 1] + (F(x[i - 1]) + y[i - 1] - kappa * v[i - 1]) * deltat

    if numpy.isnan(x[-1]) or numpy.absolute(x[-1]) > 1000000000:
        print('Trajectroy Blew out!')
        return

    outDict = {'mean': numpy.mean(x), 'median': numpy.median(x), 'std': numpy.std(x), 'range': numpy.max(x) - numpy.min(x),
               'proppos': numpy.sum((x > 0)) / N, 'pcross': numpy.sum((numpy.multiply(x[:-1], x[1:]) < 0)) / (N - 1),
               'ac1': numpy.absolute(CO_AutoCorr(x)), 'ac10': numpy.absolute(CO_AutoCorr(x, 10)),
               'ac25': numpy.absolute(CO_AutoCorr(x, 25)), 'tau': CO_FirstZero(x),
               'finaldev': numpy.absolute(x[-1])}

    if whatPotential == 'dblwell':
        outDict['pcrossup'] = numpy.sum((numpy.multiply(x[:-1] - alpha, x[1:] - alpha) < 0)) / (N - 1)
        outDict['pcrossdown'] = numpy.sum((numpy.multiply(x[:-1] + alpha, x[1:] + alpha) < 0)) / (N - 1)

    return outDict
