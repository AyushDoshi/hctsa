import math

import numpy
from scipy import stats

from hctsa.PeripheryFunctions import BF_buffer


def ST_MomentCorr(x, windowLength=.02, wOverlap=.2, mom1='mean', mom2='std', whatTransform='none'):
    """
    """
    N = len(x)

    if windowLength < 1:
        windowLength = math.ceil(N * windowLength)

    if wOverlap < 1:
        wOverlap = math.floor(windowLength * wOverlap)

    if whatTransform == 'abs':

        x = numpy.abs(x)

    elif whatTransform == 'sq':

        x = numpy.sqrt(x)

    elif whatTransform == 'none':

        pass

    x_buff = BF_buffer(x, windowLength, wOverlap)

    numWindows = (N / (windowLength - wOverlap))

    if x_buff.shape[1] > numWindows:
        x_buff = x_buff[:, 0:x_buff.shape[1] - 1]

    pointsPerWindow = x_buff.shape[0]

    if pointsPerWindow == 1:
        return None

    M1 = SUB_calcmemoments(x_buff, mom1)
    M2 = SUB_calcmemoments(x_buff, mom2)

    R = numpy.corrcoef(M1, M2)

    outDict = {'R': R[1, 0], 'absR': abs(R[1, 0]), 'density': (numpy.max(M1) - numpy.min(M1)) * (numpy.max(M2) - numpy.min(M2)) / N}

    return outDict


def SUB_calcmemoments(x_buff, momType):
    """
    """
    if momType == 'mean':

        moms = numpy.mean(x_buff, axis=0)

    elif momType == 'std':

        moms = numpy.std(x_buff, axis=0, ddof=1)

    elif momType == 'median':

        moms = numpy.median(x_buff, axis=0)

    elif momType == 'iqr':

        moms = stats.iqr(x_buff, axis=0)

    return moms
