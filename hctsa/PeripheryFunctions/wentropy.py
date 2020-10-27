import numpy


def wentropy(x, entType='shannon', addiontalParameter=None):
    """
    """
    if entType == 'shannon':

        x = numpy.power(x[x != 0], 2)

        return - numpy.sum(numpy.multiply(x, numpy.log(x)))

    elif entType == 'threshold':

        if addiontalParameter is None or isinstance(addiontalParameter, str):
            return None

        x = numpy.absolute(x)

        return numpy.sum((x > addiontalParameter))

    elif entType == 'norm':

        if addiontalParameter is None or isinstance(addiontalParameter, str) or addiontalParameter < 1:
            return None

        x = numpy.absolute(x)

        return numpy.sum(numpy.power(x, addiontalParameter))

    elif entType == 'sure':

        if addiontalParameter is None or isinstance(addiontalParameter, str):
            return None

        N = len(x)

        x2 = numpy.square(x)

        t2 = addiontalParameter ** 2

        xgt = numpy.sum((x2 > t2))

        xlt = N - xgt

        return N - (2 * xlt) + (t2 * xgt) + numpy.sum(numpy.multiply(x2, (x2 <= t2)))

    elif entType == 'logenergy':

        x = numpy.square(x[x != 0])

        return numpy.sum(numpy.log(x))

    else:
        print("invalid entropy type")
        return None
