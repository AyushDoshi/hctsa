import numpy


def MD_polvar(x, d=1, D=6):
    """
    """
    dx = numpy.absolute(numpy.diff(x))

    N = len(dx)

    xsym = (dx >= d)
    zseq = numpy.zeros(D)
    oseq = numpy.ones(D)

    i = 1
    pc = 0

    while i <= (N - D):

        xseq = xsym[i:(i + D)]

        if numpy.sum((xseq == zseq)) == D or numpy.sum((xseq == oseq)) == D:

            pc += 1
            i += D

        else:

            i += 1

    p = pc / N

    return p
