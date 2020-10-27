import numpy
from scipy import stats


def DN_CompareKSFit(x, whatDist='norm'):
    """
    """
    xStep = numpy.std(x) / 100
    if whatDist == 'norm':
        a, b = stats.norm.fit(x)
        peak = stats.norm.pdf(a, a, b)
        thresh = peak / 100
        xf1 = numpy.mean(x)
        ange = 10
        while ange > thresh:
            xf1 = xf1 - xStep
            ange = stats.norm.pdf(xf1, a, b)
        ange = 10
        xf2 = numpy.mean(x)
        while ange > thresh:
            xf2 = xf2 + xStep
            ange = stats.norm.pdf(xf2, a, b)

    # since some outliers real far away can take long time
    # should probably do pre-proccessing before functions
    if whatDist == "uni":

        a, b = stats.uniform.fit(x)
        peak = stats.uniform.pdf(numpy.mean(x), a, b - a)
        thresh = peak / 100
        xf1 = numpy.mean(x)
        ange = 10
        while ange > thresh:
            xf1 = xf1 - xStep
            ange = stats.norm.pdf(xf1, a, b)
        ange = 10
        xf2 = numpy.mean(x)
        while ange > thresh:
            xf2 = xf2 + xStep
            ange = stats.norm.pdf(xf2, a, b)

    # might over write y since changing x
    if whatDist == 'beta':
        scaledx = (x - numpy.min(x) + .01 * numpy.std(x)) / (numpy.max(x) - numpy.min(x) + .02 * numpy.std(x))
        xStep = numpy.std(scaledx) / 100
        a = stats.beta.fit(scaledx)
        b = a[2]
        a = a[1]
        thresh = 1E-5
        xf1 = numpy.mean(scaledx)
        ange = 10
        while ange > thresh:
            xf1 = xf1 - xStep
            ange = stats.beta.pdf(xf1, a, b)
        ange = 10
        xf2 = numpy.mean(scaledx)
        while ange > thresh:
            xf2 = xf2 + xStep
            ange = stats.beta.pdf(xf2, a, b)
        x = scaledx

    kde = stats.gaussian_kde(x)
    test_space = numpy.linspace(numpy.min(x), numpy.max(x), 1000)
    kde_est = kde(test_space)
    if whatDist == 'norm':
        ffit = stats.norm.pdf(test_space, a, b)
    if whatDist == 'uni':
        ffit = stats.uniform.pdf(test_space, a, b - a)
    if whatDist == 'beta':
        ffit = stats.beta.pdf(test_space, a, b)

    out = {'adiff': sum(numpy.absolute(kde_est - ffit) * (test_space[1] - test_space[0])),
           'peaksepy': numpy.max(ffit) - numpy.max(kde_est)}

    r = (ffit != 0)

    out['relent'] = sum(
        numpy.multiply(kde_est[r], numpy.log(numpy.divide(kde_est[r], ffit[r]))) * (test_space[1] - test_space[0]))

    return out
