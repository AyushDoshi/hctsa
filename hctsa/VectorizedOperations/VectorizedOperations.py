import numpy
from scipy import stats


def DN_RemovePointsVect(y, removeHow='absfar', p=.1, acf_y=None, FirstZero=None):
    """
    """
    if removeHow == 'absclose':

        i = numpy.argsort(-numpy.absolute(y), kind='mergesort', axis=1)

    elif removeHow == 'absfar':

        i = numpy.argsort(numpy.absolute(y), kind='mergesort', axis=1)

    elif removeHow == 'min':

        i = numpy.argsort(-y, kind='mergesort', axis=1)

    elif removeHow == 'max':

        i = numpy.argsort(y, kind='mergesort', axis=1)

    N = y.shape[1]
    points = y.shape[0]

    out = numpy.zeros((points, 13))

    rKeep = numpy.sort(i[:, 0:int(numpy.round(N * (1 - p)))], axis=1)

    y_trim = numpy.zeros(rKeep.shape)

    for i in range(points):
        y_trim[i, :] = y[i, rKeep[i, :]]

    if acf_y is None:
        acf_y = SUB_acf(y, 8)

    acf_y_trim = SUB_acf(y_trim, 8)

    if FirstZero is None:
        FirstZero = CO_FirstZeroVect(y)

    out[:, 0] = numpy.divide(CO_FirstZeroVect(y_trim), FirstZero).flatten()

    out[:, 1] = numpy.divide(acf_y_trim[:, 0], acf_y[:, 0]).flatten()

    out[:, 2] = numpy.absolute(acf_y_trim[:, 0] - acf_y[:, 0])

    out[:, 3] = numpy.divide(acf_y_trim[:, 1], acf_y[:, 1]).flatten()

    out[:, 4] = numpy.absolute(acf_y_trim[:, 1] - acf_y[:, 1])

    out[:, 5] = numpy.divide(acf_y_trim[:, 2], acf_y[:, 2]).flatten()

    out[:, 6] = numpy.absolute(acf_y_trim[:, 2] - acf_y[:, 2])

    out[:, 7] = numpy.sum(numpy.absolute(acf_y_trim - acf_y), axis=1)

    out[:, 8] = numpy.mean(y_trim, axis=1)

    out[:, 9] = numpy.median(y_trim, axis=1)

    out[:, 10] = numpy.std(y_trim)

    out[:, 11] = numpy.divide(stats.skew(y_trim, axis=1), stats.skew(y, axis=1))

    out[:, 12] = numpy.divide(stats.kurtosis(y_trim, axis=1, fisher=False), stats.kurtosis(y, axis=1, fisher=False))

    return out


def SUB_acf(x, n):
    """
    """
    acf = numpy.zeros((x.shape[0], n))

    for i in range(n):
        acf[:, i] = CO_AutoCorrVect(x, i)

    return acf


def CO_FirstZeroVect(y, minWhat='ac'):
    """
    """
    acf = CO_AutoCorrVect(y, [])

    N = y.shape[1]

    points = y.shape[0]

    result = numpy.zeros((points, 1))

    for i in range(1, N - 1):

        # update result if current if less than before
        # and that rows first min wasnt already found

        less = (acf[:, i] <= 0).reshape((points, 1))

        notseen = (result == 0)

        result[numpy.logical_and(less, notseen)] = i

        if numpy.logical_not(notseen).all():
            return result

    result[notseen] = N

    return result


def CO_FirstMinVect(y, minWhat='ac'):
    """
    """
    acf = CO_AutoCorrVect(y, [])

    N = y.shape[1]

    points = y.shape[0]

    result = numpy.zeros((points, 1))

    for i in range(1, N - 1):

        # update result if current if less than before
        # and that rows first min wasnt already found

        less = (acf[:, i] - acf[:, i - 1] < 0).reshape((points, 1))

        notseen = (result == 0)

        result[numpy.logical_and(less, notseen)] = i

        if numpy.logical_not(notseen).all():
            return result

    result[notseen] = N

    return result


def CO_AutoCorrVect(y, lag=1, method='Fourier', t=1, mean=None, std=None):
    """
    """
    if mean is None:
        mean = numpy.mean(y, axis=1)
        mean = mean.reshape((mean.shape[0], 1))

    if std is None:
        std = numpy.std(y, axis=1)

    def ACFy(tau):
        """
        """
        return numpy.divide(numpy.mean(numpy.multiply((y[:, :-tau] - mean), (y[:, tau:] - mean)), axis=1), numpy.power(std, 2))

    if method == 'TimeDomianStat':

        if not lag:

            acf = numpy.zeros((y.shape[1], 26))

            acf[:, 0] = 1

            for i in range(1, 26):
                acf[:, i] = ACFy(i)

            return acf

        return ACFy(lag)

    N = y.shape[1]

    points = y.shape[0]

    nFFT = int(2 ** (numpy.ceil(numpy.log2(N)) + 1))

    F = numpy.fft.fft(y - mean, nFFT, axis=1)

    F = numpy.multiply(F, numpy.conj(F))

    acf = numpy.fft.ifft(F, axis=1)

    acf = numpy.divide(acf, acf[:, 0].reshape((points, 1)))

    acf = acf.real

    if not lag:
        return acf

    return acf[:, lag]


def DN_BurstinessVect(y, mean=None, std=None):
    """
    """
    if mean is None:
        mean = numpy.mean(y, axis=1)

    if std is None:
        std = numpy.std(y, axis=1)

    r = numpy.divide(std, mean)

    B = numpy.divide((r - 1), (r + 1))

    return B


def CO_NonlinearAutocorrVect(y, taus, doAbs='empty'):
    """
    """
    if doAbs == 'empty':

        if len(taus) % 2 == 1:

            doAbs = 0

        else:

            doAbs = 1

    N = int(y.shape[1])

    tmax = numpy.max(taus)

    nlac = y[:, tmax:N]

    for i in taus:
        nlac = numpy.multiply(nlac, y[:, tmax - i:N - i])

    if doAbs:
        return numpy.mean(numpy.absolute(nlac), axis=1)

    return numpy.mean(nlac, axis=1)
