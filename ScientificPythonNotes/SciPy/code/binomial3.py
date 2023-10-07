from scipy.stats import binom
from scipy.optimize import bisect

def binomial_ci( mle, N, alpha=0.05 ):
    """
    One sided confidence interval for a binomial test.

    If after N trials we obtain mle as the proportion of those
    trials that resulted in success, find c such that

    P(k/N < mle; theta = c) = alpha

    where k/N is the proportion of successes in the set of trials,
    and theta is the success probability for each trial. 
    """


    to_minimise = lambda c: binom.cdf(mle*N,N,c)-alpha
    return bisect(to_minimise,0,1)


def binomial_ci2(x, n, alpha=0.05):
    #x is number of successes, n is number of trials
    from scipy import stats
    if x==0:
        c1 = 0
    else:
        c1 = stats.beta.interval(1-alpha, x,n-x+1)[0]
    if x==n:
        c2=1
    else:
        c2 = stats.beta.interval(1-alpha, x+1,n-x)[1]
    return c1, c2
