from matplotlib import pyplot as plt 
from __future__ import division
from collections import defaultdict, Counter
import math

from Chapter4_Linear_Algebra import sum_of_squares, dot_multiply

num_friends = [100,60 ,49, 41, 40, 25, 25, 20, 20, 18, 18, 15, 15, 15, 15, 15, 14, 13, 12, 11, 11, 11, 11, 11, 10, 5, 1]
num_minutes = [5, 70, 55, 50, 50, 48, 47, 50, 35, 38, 33, 20, 19, 15, 22, 21, 19, 18, 19, 20, 15, 13, 12, 11, 5, 5]


friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs,ys)
plt.axis([0, 101, 0, 15])
plt.title("Histogram of friend counts")
plt.xlabel("# of people")
plt.show()

num_points = len(num_friends)
print num_points

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
largest_value = sorted_values[-1]
second_largest_value = sorted_values[-2]
print second_largest_value

def mean(x):
    return sum(x) / len(x)

mean(num_friends)

def median(v):
    n = len(v)
    sorted_v = sorted(v)

    if n % 2 == 1:
        return sorted_v[n / 2]
    else:
        lo = sorted_v[n // 2 -1]
        hi = sorted_v[n // 2]
        return (hi + lo) / 2

median(num_friends)

def quantile(x, p):
    p_index = int(p *len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.1)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.9)

def mode(v):
    counts = Counter(v)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
            if count == max_count]

mode(num_friends)

def data_range(v):
    return max(v) - min (v)

data_range(num_friends)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

variance(num_friends)

def standard_deviation(x):
    return math.sqrt(variance(x))

standard_deviation(num_friends)

def interquantile_range(x):
    return quantile (x, 0.75) - quantile(x, 0.25)

interquantile_range(num_friends)    

def covariance(x, y):
    n = len(x)
    return dot_multiply(de_mean(x), de_mean(y)) / (n - 1)

covariance(num_friends, num_minutes)

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x,y) / stdev_x / stdev_y
    else:
        return 0

correlation(num_friends, num_minutes)

plt.scatter(num_friends, num_minutes)

plt.title("Daily Minutes cs. Number of friends")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()

## there is a "wrong account" because of the example, the 100 friends guy, so we can eliminate him

outlier = num_friends.index(100)

num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]

num_minutes_good = [x
                    for i, x in enumerate(num_minutes)
                    if i != outlier]

correlation(num_friends_good, num_minutes_good)


plt.scatter(num_friends_good, num_minutes_good)

plt.title("Correlation after removing the outlier")
plt.xlabel("# of friends")
plt.ylabel("daily minutes spent on the site")
plt.show()