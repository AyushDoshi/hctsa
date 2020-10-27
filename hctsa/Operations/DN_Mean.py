# @numba.jit(nopython=True,parallel=True)
def DN_Mean(y):
    """
    """
    # y must be numpy array
    # if not isinstance(y,numpy.ndarray):
    #     y = numpy.asarray(y)
    return y.mean()
