import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Dataset
age = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
fat = [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

# Create DataFrame
data = pd.DataFrame({
    'Age': age,
    'BodyFat': fat
})

# -------------------------
# 1. Mean, Median, Std Dev
# -------------------------
print("Mean:\n", data.mean())
print("\nMedian:\n", data.median())
print("\nStandard Deviation:\n", data.std())

# -------------------------
# 2. Boxplots
# -------------------------
plt.figure()
data.boxplot(column=['Age','BodyFat'])
plt.title("Boxplot of Age and Body Fat")
plt.show()

# -------------------------
# 3. Scatter Plot
# -------------------------
plt.figure()
plt.scatter(data['Age'], data['BodyFat'])
plt.xlabel("Age")
plt.ylabel("Body Fat %")
plt.title("Age vs Body Fat")
plt.show()

# -------------------------
# 4. Q-Q Plot
# -------------------------
plt.figure()
stats.probplot(data['BodyFat'], dist="norm", plot=plt)
plt.title("Q-Q Plot for Body Fat")
plt.show()
