import math

# Normal Probability Density Function (PDF)
def norm_pdf(x, mean=0, std=1):
    return (1 / (std * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mean) / std) ** 2)

# Cumulative Distribution Function (CDF)
def norm_cdf(x, mean=0, std=1):
    return 0.5 * (1 + math.erf((x - mean) / (std * math.sqrt(2))))

# Example: CDF at x = 1.96 for standard normal N(0,1)
print(norm_cdf(1.96))  # Outputs ~0.975