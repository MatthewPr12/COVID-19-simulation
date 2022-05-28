import scipy.stats


def get_normal_distribution():
    lower = 0
    upper = 1
    mu = 0.5
    sigma = 0.2
    N = 1
    return [item * 90 for item in list(scipy.stats.truncnorm.rvs(
        (lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma, size=N))]


print(get_normal_distribution())
