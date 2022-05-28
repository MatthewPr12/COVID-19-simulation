import scipy.stats


def get_normal_distribution():
    lower = 0
    upper = 1
    mu = 0.5
    sigma = 0.2
    N = 10000
    return list(scipy.stats.truncnorm.rvs(
        (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=N))
