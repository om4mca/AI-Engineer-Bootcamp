from scipy.stats import norm

x = 70

density = norm.pdf(
    x,
    loc=70,
    scale=10
)

print(density)

probability = norm.cdf(
    80,
    loc=70,
    scale=10
)

print(probability)