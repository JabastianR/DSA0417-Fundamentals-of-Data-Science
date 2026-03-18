import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Example data (blood pressure reduction)
control = np.array([5, 6, 4, 5, 6, 5, 4, 6, 5, 5])
treatment = np.array([10, 12, 11, 13, 12, 11, 10, 12, 13, 11])

# -------------------------
# Hypothesis Testing
# -------------------------
# H0: No difference between groups
# H1: Significant difference exists

t_stat, p_value = stats.ttest_ind(treatment, control)

print("T-statistic:", t_stat)
print("P-value:", p_value)

# Decision
alpha = 0.05
if p_value < alpha:
    print("Reject Null Hypothesis: Treatment is effective")
else:
    print("Fail to Reject Null Hypothesis: No significant effect")

# -------------------------
# Visualization
# -------------------------

# Boxplot comparison
plt.figure()
plt.boxplot([control, treatment], labels=["Control", "Treatment"])
plt.title("Control vs Treatment Comparison")
plt.ylabel("Blood Pressure Reduction")
plt.show()

# Bar plot of means
means = [np.mean(control), np.mean(treatment)]

plt.figure()
plt.bar(["Control", "Treatment"], means)
plt.title("Mean Comparison (p-value = {:.4f})".format(p_value))
plt.ylabel("Average Reduction")
plt.show()
