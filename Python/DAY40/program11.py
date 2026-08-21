from scipy import stats

mu, sigma = 0, 1
dist = stats.norm(loc=mu, scale=sigma)

# Exact tail-to-tail integrations
p_1sigma = dist.cdf(1) - dist.cdf(-1)
p_2sigma = dist.cdf(2) - dist.cdf(-2)
p_3sigma = dist.cdf(3) - dist.cdf(-3)

print("--- EXACT THEORETICAL VALUES ---")
print(f"P(μ - 1σ <= X <= μ + 1σ): {p_1sigma:.6f} ({p_1sigma:.4%})")
print(f"P(μ - 2σ <= X <= μ + 2σ): {p_2sigma:.6f} ({p_2sigma:.4%})")
print(f"P(μ - 3σ <= X <= μ + 3σ): {p_3sigma:.6f} ({p_3sigma:.4%})")