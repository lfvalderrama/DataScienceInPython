from __future__ import division # integer division is lame

import random
import math
from matplotlib import pyplot as plt 
from collections import defaultdict, Counter

from Chapter6_probability import normal_cdf, inverse_normal_cdf

def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


# the normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf

# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probability"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z >= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probability above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


##Test about the hypotesis of a fair coin, flipping the coin n = 1000 times, if the hypothesis is true, it should have a normal distribution with mean 50
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# 95% bounds based on assumption p is 0.5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

# a type 2 error means we fail to reject the null hypothesis
# which will happen when X is still in our original interval
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
1 - type_2_probability # 0.887

#H0 P<=0.5
hi = normal_upper_bound(0.95, mu_0, sigma_0)

# is 526 (< 531, since we need more probability in the upper tail)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability # 0.936


def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
    # if x is greater than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
    # if x is less than the mean, the tail is what's less than x
        return 2 * normal_probability_below(x, mu, sigma)

#If we were to see 530 heads, we would compute:
two_sided_p_value(529.5, mu_0, sigma_0) # 0.062

extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0 # count # of heads
                    for _ in range(1000)) # in 1000 flips
    if num_heads >= 530 or num_heads <= 470: # and count how often
        extreme_value_count += 1 # the # is 'extreme'

print extreme_value_count / 100000 # 0.062 not rejected because > than the 5%

two_sided_p_value(531.5, mu_0, sigma_0) # 0.0463 rejected because less than the 5%

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

#For our one-sided test, if we saw 525 heads we would compute:
upper_p_value(524.5, mu_0, sigma_0) # 0.061 -> not rejected
#which means we wouldn’t reject the null. If we saw 527 heads, the computation would be:
upper_p_value(526.5, mu_0, sigma_0) # 0.047 -> rejected

def B(alpha, beta):
    """a normalizing constant so that the total probability is 1"""
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)
def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1: # no weight outside of [0, 1]
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta - 1) / B(alpha, beta)