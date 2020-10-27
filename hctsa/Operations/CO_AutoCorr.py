import numpy


def CO_AutoCorr(y, lag=1, method='Fourier', t=1):
    """
    """
    # if not isinstance(y,numpy.ndarray):
    #     y = numpy.asarray(y)

    if method == 'TimeDomainStat':

        if not lag:

            acf = [1]

            for i in range(1, len(y) - 1):
                acf.append(numpy.corrcoef(y[:-i], y[i:])[0, 1])

            return acf

        return numpy.corrcoef(y[:-lag], y[lag:])[0, 1]

    else:

        N = len(y)

        nFFT = int(2 ** (numpy.ceil(numpy.log2(N)) + 1))

        F = numpy.fft.fft(y - y.mean(), nFFT)

        F = numpy.multiply(F, numpy.conj(F))

        acf = numpy.fft.ifft(F)

        if acf[0] == 0:

            if not lag:
                return acf

            return acf[lag]

        acf = acf / acf[0]
        acf = acf.real

        if not lag:
            return acf

        if lag > N:
            pass
            # print("Lag larger than series")

            return

        return acf[lag]
