import numpy


def SC_DFA(y):
    """
    """
    N = len(y)

    tau = int(numpy.floor(N / 2))

    y -= numpy.mean(y)

    x = numpy.cumsum(y)

    taus = numpy.arange(5, tau + 1)

    ntau = len(taus)

    F = numpy.zeros(ntau)

    for i in range(ntau):

        t = int(taus[i])

        x_buff = x[:N - N % t]

        x_buff = x_buff.reshape((int(N / t), t))

        y_buff = numpy.zeros((int(N / t), t))

        for j in range(int(N / t)):
            tt = range(0, int(t))

            p = numpy.polyfit(tt, x_buff[j, :], 1)

            y_buff[j, :] = numpy.power(x_buff[j, :] - numpy.polyval(p, tt), 2)

        y_buff.reshape((N - N % t, 1))

        F[i] = numpy.sqrt(numpy.mean(y_buff))

    logtaur = numpy.log(taus)

    logF = numpy.log(F)

    p = numpy.polyfit(logtaur, logF, 1)

    return p[0]
