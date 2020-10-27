# import matplotlib.pyplot as plt
import numpy


def SC_HurstExp(x):
    """
    """
    N = len(x)

    splits = int(numpy.log2(N))

    rescaledRanges = []

    n = []

    for i in range(splits):
        chunks = 2 ** i

        n.append(int(N / chunks))

        y = x[:N - N % chunks]

        y = y.reshape((chunks, int(N / chunks)))

        m = y.mean(axis=1, keepdims=True)

        y = y - m

        z = numpy.cumsum(y, 1)

        R = numpy.max(z, 1) - numpy.min(z, 1)

        S = numpy.std(y, 1)

        S[S == 0] = 1

        rescaledRanges.append(numpy.mean(R / S))

    logRS = numpy.log(rescaledRanges)
    logn = numpy.log(n)

    # plt.plot(logn,logRS)
    # plt.show()

    p = numpy.polyfit(logn, logRS, 1)

    return p[0]
