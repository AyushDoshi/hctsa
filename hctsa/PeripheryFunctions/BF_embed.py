import numpy

from hctsa.Operations import CO_FirstZero


def BF_embed(y, tau=1, m=2, makeSignal=0, randomSeed=None, beVocal=0):
    """
    """
    if randomSeed is None:
        randomSeed = []
    N = len(y)

    if tau == 'ac':
        tau = CO_FirstZero(y)

    if m == 'fnnsmall':
        th = .01

    N_embed = N - (m - 1) * tau

    if N_embed <= 0:
        raise Exception('Time Series (N = %u) too short to embed with these embedding parameters')
    y_embed = numpy.zeros((N_embed, m))

    for i in range(1, m + 1):
        y_embed[:, i - 1] = y[(i - 1) * tau:N_embed + (i - 1) * tau]
    return y_embed
