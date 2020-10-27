import numpy


def DN_OutlierTest(y, p=2, justMe=''):
    """
    """
    outDict = {}

    index = numpy.logical_and(y > numpy.percentile(y, p), y < numpy.percentile(y, 100 - p))

    outDict['mean'] = numpy.mean(y[index])

    outDict['std'] = numpy.std(y[index], ddof=1) / numpy.std(y, ddof=1)

    if justMe == 'mean':

        return outDict['mean']

    elif justMe == 'std':

        return outDict['std']

    return outDict
