import scipy.stats as stats

# Standard Normal Distribution CDF calculations
prob_1sd = stats.norm.cdf(1) - stats.norm.cdf(-1)
prob_2sd = stats.norm.cdf(2) - stats.norm.cdf(-2)
prob_3sd = stats.norm.cdf(3) - stats.norm.cdf(-3)

print(f"1 SD (|Z| <= 1): {prob_1sd:.6f} ({prob_1sd*100:.4f}%)")
print(f"2 SD (|Z| <= 2): {prob_2sd:.6f} ({prob_2sd*100:.4f}%)")
print(f"3 SD (|Z| <= 3): {prob_3sd:.6f} ({prob_3sd*100:.4f}%)")