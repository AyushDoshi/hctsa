# author: Dominik Krzeminski (dokato)
# https://github.com/dokato/dfa


# detrended fluctuation analysis
import numpy


def calc_rms(x, scale):
    """
    windowed Root Mean Square (RMS) with linear detrending.

    Args:
    -----
      *x* : numpy.array
        one dimensional data vector
      *scale* : int
        length of the window in which RMS will be calculaed
    Returns:
    --------
      *rms* : numpy.array
        RMS data in each window with length len(x)//scale
    """
    # making an array with data divided in windows
    shape = (x.shape[0] // scale, scale)
    X = numpy.lib.stride_tricks.as_strided(x, shape=shape)
    # vector of x-axis points to regression
    scale_ax = numpy.arange(scale)
    rms = numpy.zeros(X.shape[0])
    for e, xcut in enumerate(X):
        coeff = numpy.polyfit(scale_ax, xcut, 1)
        xfit = numpy.polyval(coeff, scale_ax)
        # detrending and computing RMS of each window
        rms[e] = numpy.sqrt(numpy.mean((xcut - xfit) ** 2))
    return rms


def dfa(x, scale_lim=None, scale_dens=0.25, show=False):
    """
    Detrended Fluctuation Analysis - measures power law scaling coefficient
    of the given signal *x*.

    More details about the algorithm you can find e.g. here:
    Hardstone, R. et al. Detrended fluctuation analysis: A scale-free
    view on neuronal oscillations, (2012).

    Args:
    -----
      *x* : numpy.array
        one dimensional data vector
      *scale_lim* = [5,9] : list of length 2
        boundaries of the scale, where scale means windows among which RMS
        is calculated. Numbers from list are exponents of 2 to the power
        of X, eg. [5,9] is in fact [2**5, 2**9].
        You can think of it that if your signal is sampled with F_s = 128 Hz,
        then the lowest considered scale would be 2**5/128 = 32/128 = 0.25,
        so 250 ms.
      *scale_dens* = 0.25 : float
        density of scale divisions, eg. for 0.25 we get 2**[5, 5.25, 5.5, ... ]
      *show* = False
        if True it shows matplotlib log-log plot.
    Returns:
    --------
      *scales* : numpy.array
        vector of scales (x axis)
      *fluct* : numpy.array
        fluctuation function values (y axis)
      *alpha* : float
        estimation of DFA exponent
    """
    # cumulative sum of data with substracted offset
    if scale_lim is None:
        scale_lim = [5, 9]
    y = numpy.cumsum(x - numpy.mean(x))
    scales = (2 ** numpy.arange(scale_lim[0], scale_lim[1], scale_dens)).astype(numpy.int)
    fluct = numpy.zeros(len(scales))
    # computing RMS for each window
    for e, sc in enumerate(scales):
        if len(calc_rms(y, sc) ** 2) == 0:
            continue
        fluct[e] = numpy.sqrt(numpy.mean(calc_rms(y, sc) ** 2))

    # fitting a line to rms data
    coeff = numpy.polyfit(numpy.log2(scales), numpy.log2(fluct), 1)
    # if show:
    #     fluctfit = 2**numpy.polyval(coeff,numpy.log2(scales))
    #     plt.loglog(scales, fluct, 'bo')
    #     plt.loglog(scales, fluctfit, 'r', label=r'$\alpha$ = %0.2f'%coeff[0])
    #     plt.title('DFA')
    #     plt.xlabel(r'$\log_{10}$(time window)')
    #     plt.ylabel(r'$\log_{10}$<F(t)>')
    #     plt.legend()
    #     plt.show()
    # return scales, fluct, coeff[0]
    return coeff[0]