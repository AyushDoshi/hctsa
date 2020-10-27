import arch
import numpy

from statsmodels.stats.diagnostic import het_arch


def MF_GARCHFit(y, preproc=None, P=1, Q=1):
    """
    """
    y = (y - numpy.mean(y)) / numpy.std(y)

    N = len(y)

    outDict = {}

    lm, lmpval, fval, fpval = het_arch(y)

    outDict['lm'] = lm
    outDict['lmpval'] = lmpval
    outDict['fval'] = fval
    outDict['fpval'] = fpval

    model = arch.arch_model(y, p=P, q=Q)
    results = model.fit()

    # print(results.summary())

    params = results._params
    paraNames = results._names

    outDict['logl'] = results._loglikelihood
    outDict['success'] = results._optim_output['success']

    for i in range(len(params)):
        outDict[paraNames[i]] = params[i]

    # pprint(vars(results))

    return outDict
