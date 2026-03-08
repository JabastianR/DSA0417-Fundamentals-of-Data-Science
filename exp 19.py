import numpy as np
from scipy import stats

# Example data (blood pressure reduction values)
drug = np.array([12,15,14,10,13,16,14,12,15,11])
placebo = np.array([5,6,4,7,5,6,5,4,6,5])

# Function to calculate 95% confidence interval
def confidence_interval(data):
    mean = np.mean(data)
    sem = stats.sem(data)   # standard error
    ci = stats.t.interval(0.95, len(data)-1, loc=mean, scale=sem)
    return mean, ci

# Drug group
mean_drug, ci_drug = confidence_interval(drug)

# Placebo group
mean_placebo, ci_placebo = confidence_interval(placebo)

print("Drug Group Mean:", mean_drug)
print("95% CI for Drug Group:", ci_drug)

print("\nPlacebo Group Mean:", mean_placebo)
print("95% CI for Placebo Group:", ci_placebo)
