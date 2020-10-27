import itertools

# import numba

# @numba.jit(nopython=True,parallel=True)
import math

import numpy

from hctsa.PeripheryFunctions import BF_embed


def EN_PermEn(y, m=2, tau=1):
    """
    """
    try:

        x = BF_embed(y, tau, m)

    except:

        return numpy.nan

    Nx = x.shape[0]

    permList = perms(m)
    numPerms = len(permList)

    countPerms = numpy.zeros(numPerms)

    for j in range(Nx):

        ix = numpy.argsort(x[j, :])

        for k in range(numPerms):

            if (permList[k, :] - ix == numpy.zeros(m)).all():
                countPerms[k] += 1

                break

    p = countPerms / Nx

    p_0 = p[p > 0]

    permEn = -sum(numpy.multiply(p_0, numpy.log2(p_0)))

    mFact = math.factorial(m)

    normPermEn = permEn / numpy.log2(mFact)

    p_LE = numpy.maximum(numpy.repeat(1 / Nx, p.shape), p)

    permENLE = - numpy.sum(numpy.multiply(p_LE, numpy.log(p_LE))) / (m - 1)

    out = {'permEn': permEn, 'normPermEn': normPermEn, 'permEnLE': permENLE}

    return out


def perms(n):
    """
    """
    permut = itertools.permutations(numpy.arange(n))

    permut_array = numpy.empty((0, n))

    for p in permut:
        permut_array = numpy.append(permut_array, numpy.atleast_2d(p), axis=0)

    return permut_array
