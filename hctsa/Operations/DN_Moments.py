import numpy
from scipy import stats


def DN_Moments(y, theMom=1):
    """
    """
    if numpy.std(y) != 0:
        return stats.moment(y, theMom) / numpy.std(y)
    else:
        return 0
