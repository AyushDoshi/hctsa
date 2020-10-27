# @numba.jit(nopython=True,parallel=True)
import numpy


def EN_ApEn(y, mnom=1, rth=.2):
    """
    """
    r = rth * numpy.std(y)
    N = len(y)
    phi = numpy.zeros(2)

    for k in range(2):
        m = mnom + k
        m = int(m)
        C = numpy.zeros(N - m + 1)

        x = numpy.zeros((N - m + 1, m))

        for i in range(N - m + 1):
            x[i, :] = y[i:i + m]

        ax = numpy.ones((N - m + 1, m))
        for i in range(N - m + 1):

            for j in range(m):
                ax[:, j] = x[i, j]

            d = numpy.absolute(x - ax)
            if m > 1:
                d = numpy.maximum(d[:, 0], d[:, 1])
            dr = (d <= r)
            C[i] = numpy.sum(dr) / (N - m + 1)
        phi[k] = numpy.mean(numpy.log(C))
    return phi[0] - phi[1]
