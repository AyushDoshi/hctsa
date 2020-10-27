import numpy
from scipy import optimize


def DT_IsSeasonal(y):
    """
    """
    N = len(y)

    th_fit = 0.3
    th_ampl = 0.5

    try:
        params, params_covariance = optimize.curve_fit(test_func, numpy.arange(N), y, p0=[10, 13, 600, 0])
    except:
        return False

    a, b, c, d = params

    y_pred = a * numpy.sin(b * numpy.arange(N) + d) + c

    SST = sum(numpy.power(y - numpy.mean(y), 2))
    SSr = sum(numpy.power(y - y_pred, 2))

    R = 1 - SSr / SST

    if R > th_fit:  # and (numpy.absolute(a) > th_ampl*.1*numpy.std(y)):
        return True
    else:
        return False


def test_func(x, a, b, c, d):
    return a * numpy.sin(b * x + d) + c
