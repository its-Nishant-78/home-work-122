import scipy.stats as stats
x = 3
n = 10
p = 0.5
prob_1 = stats.binom.pmf(x, n, p)
print("Probability of getting 3 heads:", prob_1)
prob_2 = 1 - stats.binom.cdf(2, n, p)
print("Probability of getting more than 2 heads:", prob_2)