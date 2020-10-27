import numpy
from scipy import stats

from hctsa.PeripheryFunctions import BF_sgnchange


def DN_FitKernalSmooth(x, varargin=None):
    """
    """
    # varargin should be dict with possible keys numcross
    # area and arclength

    if varargin is None:
        varargin = {}
    out = {}

    m = numpy.mean(x)

    kde = stats.gaussian_kde(x)
    # i think matlabs kde uses 100 points
    # but end numbers end up being midly off
    # seems to be rounding entropy max, min line up
    test_space = numpy.linspace(numpy.min(x), numpy.max(x), 100)

    f = kde(test_space)

    df = numpy.diff(f)

    ddf = numpy.diff(df)

    sdsp = ddf[BF_sgnchange(df, 1)]

    out['npeaks'] = sum(sdsp < -.0002)

    out['max'] = numpy.max(f)

    out['entropy'] = - sum(numpy.multiply(f[f > 0], numpy.log(f[f > 0]))) * (test_space[2] - test_space[1])

    out1 = sum(f[test_space > m]) * (test_space[2] - test_space[1])
    out2 = sum(f[test_space < m]) * (test_space[2] - test_space[1])
    out['asym'] = out1 / out2

    out1 = sum(numpy.absolute(numpy.diff(f[test_space < m]))) * (test_space[2] - test_space[1])
    out1 = sum(numpy.absolute(numpy.diff(f[test_space > m]))) * (test_space[2] - test_space[1])
    out['plsym'] = out1 / out2

    if 'numcross' in varargin:
        thresholds = varargin['numcross']
        out['numCrosses'] = {}
        for i in range(len(thresholds)):
            numCrosses = sum(BF_sgnchange(f - thresholds[i]))
            out['numCrosses'][thresholds[i]] = numCrosses
    if 'area' in varargin:
        thresholds = varargin['area']
        out['area'] = {}
        for i in range(len(thresholds)):
            areaHere = sum(f[f < thresholds[i]]) * (test_space[2] - test_space[1])
            out['area'][thresholds[i]] = areaHere
    if 'arclength' in varargin:
        thresholds = varargin['arclength']
        out['arclength'] = {}
        for i in range(len(thresholds)):
            fd = numpy.absolute(numpy.diff(f[(test_space > m - thresholds[i]) & (test_space < m + thresholds[i])]))
            arclengthHere = sum(fd) * (test_space[2] - test_space[1])
            out['arclength'][thresholds[i]] = arclengthHere
    return out
