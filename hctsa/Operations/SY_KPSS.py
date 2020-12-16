from statsmodels.tsa.stattools import kpss


def SY_KPSS(ts, regression="c", nlags='auto'):
    """
    Wraper funciton to use statsmodels' KPSS function
    """
    kpss_stat, p_val, lags, crit = kpss(ts, regression=regression, nlags=nlags)
    return {'KPSS Stat': kpss_stat, 'p-value': p_val, 'lags': lags, '10% Critical Value': crit['10%'],
            '5% Critical Value': crit['5%'], '2.5% Critical Value': crit['2.5%'], '1% Critical Value': crit['1%']}
