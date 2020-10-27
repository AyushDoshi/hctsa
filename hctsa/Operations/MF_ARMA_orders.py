from statsmodels.tsa.arima_model import ARIMA
import numpy


def MF_ARMA_orders(y, pr=None, qr=None):
    """
    """
    if pr is None:
        pr = [1, 2, 3, 4, 5]
    if qr is None:
        qr = [0, 1, 2, 3, 4, 5]
    y = (y - numpy.mean(y)) / numpy.std(y)

    aics = numpy.zeros((len(pr), len(qr)))
    bics = numpy.zeros((len(pr), len(qr)))

    for i in range(len(pr)):

        for j in range(len(qr)):

            p = pr[i]
            q = qr[i]

            try:

                model = ARIMA(y, order=(p, 0, q))
                model_fit = model.fit(disp=False)

            except:
                print("FAILED ARMA MODEL")
                return None
            aics[i, j] = model_fit.aic
            bics[i, j] = model_fit.bic

    outDict = {'aic_min': numpy.min(aics)}

    mins = numpy.argwhere(aics == numpy.min(aics))[0]

    outDict['opt_p'] = pr[mins[0]]

    outDict['opt_q'] = qr[mins[0]]

    outDict['meanAICS'] = numpy.mean(aics)
    outDict['stdAICS'] = numpy.std(aics)

    outDict['meanBICS'] = numpy.mean(bics)
    outDict['stdBICS'] = numpy.std(bics)

    return outDict
