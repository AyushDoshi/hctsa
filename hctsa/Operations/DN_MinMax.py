# @numba.jit(nopython=True,parallel=True)
def DN_MinMax(y, which='max'):
    """
    """
    # if not isinstance(y,numpy.ndarray):
    #     y = numpy.asarray(y)
    if which == 'min':
        return y.min()
    else:
        return y.max()
