import scipy.stats

lower = 0
upper = 1
mu = 0.5
sigma = 0.2
N = 10000


def get_normal_distribution():
    return list(scipy.stats.truncnorm.rvs(
        (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=N)) * 90
