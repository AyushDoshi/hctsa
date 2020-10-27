import math

import numpy


def ZG_hmm_cl(X, T, K, Mu, Cov, P, Pi):
    """
    """
    p = 1

    N = len(X)

    tiny = numpy.exp(-700)

    if N % T != 0:
        print('N not % T')

        return None

    N = int(N / T)

    alpha = numpy.zeros((T, K))
    B = numpy.zeros((T, K))

    k1 = (2 * math.pi) ** (-p / 2)

    Scale = numpy.zeros((1, T))

    likv = numpy.zeros((1, N))

    for n in range(int(N)):

        B = numpy.zeros((T, K))
        iCov = 1 / Cov

        k2 = k1 / math.sqrt(Cov)

        for i in range(T):

            for l in range(K):
                d = Mu[l] - X[(n - 1) * T + i]
                B[i, l] = k2 * numpy.exp(-.5 * d * iCov * d)

        scale = numpy.zeros((T, 1))
        alpha[0, :] = numpy.multiply(Pi.flatten('F'), B[0, :])
        scale[0] = numpy.sum(alpha[0, :])
        alpha[0, :] = alpha[0, :] / scale[0]

        for i in range(1, T):
            alpha[i, :] = numpy.multiply(numpy.matmul(alpha[i - 1, :], P), B[i, :])
            scale[i] = numpy.sum(alpha[i, :])
            alpha[i, :] = alpha[i, :] / (scale[i] + tiny)

        likv[n] = numpy.sum(numpy.log(scale + (scale == 0) * tiny))
        Scale = Scale + numpy.log(scale + (scale == 0) * tiny)

    lik = numpy.sum(Scale)

    return lik, likv
