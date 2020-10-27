from scipy import signal
import numpy


def SY_Trend(y):
    """
    """
    N = len(y)
    stdRatio = numpy.std(signal.detrend(y)) / numpy.std(y)

    gradient, intercept = LinearFit(numpy.arange(N), y)

    yC = numpy.cumsum(y)
    meanYC = numpy.mean(yC)
    stdYC = numpy.std(yC)

    # print(gradient)
    # print(intercept)

    gradientYC, interceptYC = LinearFit(numpy.arange(N), yC)

    meanYC12 = numpy.mean(yC[0:int(numpy.floor(N / 2))])
    meanYC22 = numpy.mean(yC[int(numpy.floor(N / 2)):])

    out = {'stdRatio': stdRatio, 'gradient': gradient, 'intercept': intercept,
           'meanYC': meanYC, 'stdYC': stdYC, 'gradientYC': gradientYC,
           'interceptYC': interceptYC, 'meanYC12': meanYC12, 'meanYC22': meanYC22}
    return out


def LinearFit(xData, yData):
    """
    """
    m, b = numpy.polyfit(xData, yData, 1)
    return m, b
