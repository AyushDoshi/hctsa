import math

import numpy
from scipy import signal


def MD_hrv_classic(y):
    """

    classic heart rate variabilty statistics

    Typically assumes an NN/RR time series in the units of seconds

    :param y: the input time series

    Includes:
    (i) pNNx
    cf. "The pNNx files: re-examining a widely used heart rate variability
           measure", J.E. Mietus et al., Heart 88(4) 378 (2002)

    (ii) Power spectral density ratios in different frequency ranges
    cf. "Heart rate variability: Standards of measurement, physiological
        interpretation, and clinical use",
        M. Malik et al., Eur. Heart J. 17(3) 354 (1996)

    (iii) Triangular histogram index, and

    (iv) Poincare plot measures
    cf. "Do existing measures of Poincare plot geometry reflect nonlinear
       features of heart rate variability?"
        M. Brennan, et al., IEEE T. Bio.-Med. Eng. 48(11) 1342 (2001)

    Code is heavily derived from that provided by Max A. Little:
    http://www.maxlittle.net/

    """

    # Standard Defaults
    diffy = numpy.diff(y)
    N = len(y)

    # Calculate pNNx percentage ---------------------------------------------------------------------------------
    Dy = numpy.abs(diffy) * 1000

    # anonymous function to fo the PNNx calculation:
    # proportion of the difference magnitudes greater than X*sigma
    PNNxfn = lambda x: numpy.sum(Dy > x) / (N - 1)

    out = {'pnn5': PNNxfn(5), 'pnn10': PNNxfn(10), 'pnn20': PNNxfn(20), 'pnn30': PNNxfn(30),
           'pnn40': PNNxfn(40)}  # declares a dictionary to contains the outputs, instead of MATLAB struct

    # calculate PSD, DOES NOT MATCH UP WITH MATLAB -----------------------------------------------------------------
    F, Pxx = signal.periodogram(y, window=numpy.hanning(
        N))  # hanning confirmed to do the same thing as hann in matlab, periodogram() is what differs

    # calculate spectral measures such as subband spectral power percentage, LF/HF ratio etc.

    LF_lo = 0.04
    LF_hi = 0.15
    HF_lo = 0.15
    HF_hi = 0.4

    fbinsize = F[1] - F[0]

    # calculating indl, indh, indv; needed for loop for python implementation
    indl = []
    for x in F:
        if LF_lo <= x <= LF_hi:
            indl.append(1)
        else:
            indl.append(0)

    indh = []
    for x in F:
        if HF_lo <= x <= HF_hi:
            indh.append(1)
        else:
            indh.append(0)
    # print("indh: ", indh)

    indv = []
    for x in F:
        if x <= LF_lo:
            indv.append(1)
        else:
            indv.append(0)
    # print("indv: ", indv)

    # calculating lfp, hfp, and vlfp, needed for loop for python implementation
    indlPxx = []
    for i in range(0, len(Pxx)):
        if indl[i] == 1:
            indlPxx.append(Pxx[i])
    lfp = fbinsize * numpy.sum(indlPxx)
    # print()
    # print('lfp: ', lfp)

    indhPxx = []
    for i in range(0, len(Pxx)):
        if indh[i] == 1:
            indhPxx.append(Pxx[i])
    hfp = fbinsize * numpy.sum(indhPxx)
    # print('hfp: ', hfp)

    indvPxx = []
    for i in range(0, len(Pxx)):
        if indv[i] == 1:
            indvPxx.append(Pxx[i])
    vlfp = fbinsize * numpy.sum(indvPxx)
    # print('vlfp: ', vlfp)

    out['lfhf'] = lfp / hfp
    total = fbinsize * numpy.sum(Pxx)
    out['vlf'] = vlfp / total * 100
    out['lf'] = lfp / total * 100
    out['hf'] = hfp / total * 100

    # triangular histogram index: ----------------------------------------------------------------------
    numBins = 10
    hist = numpy.histogram(y, bins=numBins)
    out['tri'] = len(y) / numpy.max(hist[0])

    # Poincare plot measures ---------------------------------------------------------------------------
    rmssd = numpy.std(diffy, ddof=1)  # set delta degrees of freedom to 1 to get same result as matlab
    sigma = numpy.std(y, ddof=1)

    out["SD1"] = 1 / math.sqrt(2) * rmssd * 1000
    out["SD2"] = math.sqrt(2 * sigma ** 2 - (1 / 2) * rmssd ** 2) * 1000

    return out
    # Anonymous function to do the PNNx calculation
    # proportion of the difference magnitudes greater than X*sigma
