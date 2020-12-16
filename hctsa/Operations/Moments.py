from scipy.stats import describe


def Moments(ts):
    """
    Calculate Count/Length/Number of Observations, Min, Max, and the 4 mathematical moments
    """

    stats = describe(ts)
    return {'Length': stats.nobs, 'Min': stats.minmax[0], 'Max': stats.minmax[1], 'Mean': stats.mean,
            'Varaince': stats.variance, 'Skewness': stats.skewness, 'Kurtosis': stats.kurtosis}
