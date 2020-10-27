import math

import numpy

from hctsa.Operations import CO_FirstZero
from hctsa.PeripheryFunctions import BF_makeBuffer


def ST_LocalExtrema(y, lorf='l', n=''):
    """
    """
    if lorf == 'l' and n == '':
        n = 100
    elif n == '':
        n = 5

    N = len(y)

    if lorf == 'l':
        wl = n
    elif lorf == 'n':
        wl = math.floor(N / n)
    else:
        wl = CO_FirstZero(y)

    if wl > N or wl <= 1:
        # print('window too short or long')
        return numpy.nan

    y_buffer = BF_makeBuffer(y, wl).transpose()

    numWindows = y_buffer.shape[1]

    locmax = numpy.max(y_buffer, axis=0)

    locmin = numpy.min(y_buffer, axis=0)

    abslocmin = numpy.absolute(locmin)

    exti = numpy.where(abslocmin > locmax)

    locext = locmax

    locext[exti] = locmin[exti]

    abslocext = numpy.absolute(locext)

    out = {'meanrat': numpy.mean(locmax) / numpy.mean(abslocmin), 'medianrat': numpy.median(locmax) / numpy.median(abslocmin),
           'minmax': numpy.min(locmax), 'minabsmin': numpy.min(abslocmin),
           'minmaxonminabsmin': numpy.min(locmax) / numpy.min(abslocmin), 'meanmax': numpy.mean(locmax),
           'meanabsmin': numpy.mean(abslocmin), 'meanext': numpy.mean(locext), 'medianmax': numpy.median(locmax),
           'medianabsmin': numpy.median(abslocmin), 'medianext': numpy.median(locext), 'stdmax': numpy.std(locmax, ddof=1),
           'stdmin': numpy.std(locmin, ddof=1), 'stdext': numpy.std(locext, ddof=1), 'meanabsext': numpy.mean(abslocext),
           'medianabsext': numpy.median(abslocext), 'diffmaxabsmin': numpy.sum(numpy.absolute(locmax - abslocmin)) / numWindows,
           'uord': numpy.sum(numpy.sign(locext)) / numWindows, 'maxmaxmed': numpy.max(locmax) / numpy.median(locmax),
           'minminmed': numpy.min(locmin) / numpy.median(locmin), 'maxabsext': numpy.max(abslocext) / numpy.median(abslocext)}

    # out.zcext = ST_SimpleStats(locext,'zcross');

    return out
