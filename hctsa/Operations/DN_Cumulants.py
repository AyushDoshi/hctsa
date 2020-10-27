from scipy import stats


def DN_Cumulants(y, cumWhatMay='skew1'):
    """
    """
    if cumWhatMay == 'skew1':
        return stats.skew(y)
    elif cumWhatMay == 'skew2':
        return stats.skew(y)
    elif cumWhatMay == 'kurt1':
        return stats.kurtosis(y)
    elif cumWhatMay == 'kurt2':
        return stats.kurtosis(y)
    else:
        raise Exception('Requested Unknown cumulant must be: skew1, skew2, kurt1, or kurt2')
