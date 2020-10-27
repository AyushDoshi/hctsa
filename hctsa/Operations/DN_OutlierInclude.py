import numpy
from scipy import stats

from hctsa.PeripheryFunctions import BF_iszscored


def DN_OutlierInclude(y, thresholdHow='abs', inc=.01):
    """
    """
    if not BF_iszscored(y):
        muhat, sigmahat = stats.norm.fit(y)
        y = (y - muhat) / sigmahat
        # warnings.warn('DN_OutlierInclude y should be z scored. So just converted y to z-scores')
    N = len(y)
    if thresholdHow == 'abs':
        thr = numpy.arange(0, numpy.max(numpy.absolute(y)), inc)
        tot = N
    if thresholdHow == 'p':
        thr = numpy.arange(0, numpy.max(y), inc)
        tot = sum(y >= 0)
    if thresholdHow == 'n':
        thr = numpy.arange(0, numpy.max(-y), inc)
        tot = sum(y <= 0)
    msDt = numpy.zeros((len(thr), 6))
    for i in range(len(thr)):
        th = thr[i]

        if thresholdHow == 'abs':
            r = numpy.where(numpy.absolute(y) >= th)
        if thresholdHow == 'p':
            r = numpy.where(y >= th)
        if thresholdHow == 'n':
            r = numpy.where(y <= -th)

        Dt_exc = numpy.diff(r)

        msDt[i, 0] = numpy.mean(Dt_exc)
        msDt[i, 1] = numpy.std(Dt_exc) / numpy.sqrt(len(r))
        msDt[i, 2] = len(Dt_exc) / tot * 100
        msDt[i, 3] = numpy.median(r) / (N / 2) - 1
        msDt[i, 4] = numpy.mean(r) / (N / 2) - 1
        msDt[i, 5] = numpy.std(r) / numpy.sqrt(len(r))

        return msDt
