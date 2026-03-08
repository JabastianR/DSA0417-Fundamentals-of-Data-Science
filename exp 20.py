import numpy as np
from scipy import stats

# Example conversion rate data
design_A = np.array([0.12,0.15,0.14,0.13,0.16,0.11,0.14])
design_B = np.array([0.18,0.20,0.17,0.19,0.21,0.18,0.20])

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(design_A, design_B)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision
alpha = 0.05

if p_value < alpha:
    print("There is a statistically significant difference between Design A and B")
else:
    print("No statistically significant difference between Design A and B")
