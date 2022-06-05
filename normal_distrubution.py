"""
module to get normal distribution array
"""
import scipy.stats  # pylint:disable=import-error


def get_normal_distribution():
    """
    get normal distribution array
    @return:
    """
    lower = 0
    upper = 1
    mu_coef = 0.5
    sigma = 0.2
    num = 10000
    return list(scipy.stats.truncnorm.rvs(
        (lower - mu_coef) / sigma, (upper - mu_coef) / sigma, loc=mu_coef, scale=sigma, size=num))
