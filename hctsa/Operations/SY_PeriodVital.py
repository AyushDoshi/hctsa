import numpy
from scipy import signal

def SY_PeriodVital(x):
    """
    """
    f1 = 1
    f2 = 6

    z = numpy.diff(x)

    [F, t, p] = signal.spectrogram(z, fs=60)

    f = numpy.logical_and(F >= f1, F <= f2)

    p = p[f]

    F = F[f]

    Pmean = numpy.mean(p)

    Pmax = numpy.max(p)
    ff = numpy.argmax(p)
    if ff >= len(F):
        Pf = numpy.nan
    else:
        Pf = F[ff]
    Pr = Pmax / Pmean
    Pstat = numpy.log(Pr)

    return {'Pstat': Pstat, 'Pmax': Pmax, 'Pmean': Pmean, 'Pf': Pf}
