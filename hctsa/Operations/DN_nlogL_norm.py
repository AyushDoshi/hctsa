import math

import numpy
from scipy import stats


def DN_nlogL_norm(y):
    """
    """
    muhat, sigmahat = stats.norm.fit(y)
    z = (y - muhat) / sigmahat
    L = -.5 * numpy.power(z, 2) - numpy.log(numpy.sqrt(2 * math.pi) * sigmahat)
    return -sum(L) / len(y)
