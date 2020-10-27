import numpy
from scipy import stats

from hctsa.Operations import CO_FirstZero, CO_AutoCorr


def DN_RemovePoints(y, removeHow='absfar', p=.1):
    """
    """
    if removeHow == 'absclose' or 'absclose' in removeHow:

        i = numpy.argsort(-numpy.absolute(y), kind='mergesort')

    elif removeHow == 'absfar' or 'absfar' in removeHow:

        i = numpy.argsort(numpy.absolute(y), kind='mergesort')

    elif removeHow == 'min' or 'min' in removeHow:

        i = numpy.argsort(-y, kind='mergesort')

    elif removeHow == 'max' or 'max' in removeHow:

        i = numpy.argsort(y, kind='mergesort')

    else:

        return

    N = len(y)

    out = {}

    rKeep = numpy.sort(i[0:int(numpy.round(N * (1 - p)))])
    y_trim = y[rKeep]

    # print(rKeep)

    acf_y = SUB_acf(y, 8)
    acf_y_trim = SUB_acf(y_trim, 8)

    out['fzcacrat'] = CO_FirstZero(y_trim) / CO_FirstZero(y)

    out['ac1rat'] = acf_y_trim[0] / acf_y[0]

    out['ac1diff'] = numpy.absolute(acf_y_trim[0] - acf_y[0])

    out['ac2rat'] = acf_y_trim[1] / acf_y[1]

    out['ac2diff'] = numpy.absolute(acf_y_trim[1] - acf_y[1])

    out['ac3rat'] = acf_y_trim[2] / acf_y[2]

    out['ac3diff'] = numpy.absolute(acf_y_trim[2] - acf_y[2])

    out['sumabsacfdiff'] = sum(numpy.absolute(acf_y_trim - acf_y))

    out['mean'] = numpy.mean(y_trim)

    out['median'] = numpy.median(y_trim)

    out['std'] = numpy.std(y_trim, ddof=1)

    if stats.skew(y) != 0:

        out['skewnessrat'] = stats.skew(y_trim) / stats.skew(y)

    else:

        out['skewnessrat'] = numpy.nan

    try:

        out['kurtosisrat'] = stats.kurtosis(y_trim, fisher=False) / stats.kurtosis(y, fisher=False)

    except:

        out['kurtosisrat'] = numpy.nan

    return out


def SUB_acf(x, n):
    """
    """
    acf = numpy.zeros(n)

    for i in range(n):
        acf[i] = CO_AutoCorr(x, i)

    return acf
