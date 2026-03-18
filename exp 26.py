import numpy as np
from sklearn.linear_model import LinearRegression

# Example dataset
# Features: [Area (sqft), Bedrooms]
X = np.array([
    [1200, 2],
    [1500, 3],
    [1800, 3],
    [2000, 4],
    [2200, 4],
    [2500, 5]
])

# House prices
y = np.array([200000, 250000, 280000, 320000, 350000, 400000])

# Create and train model
model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter area of the house (sqft): "))
bedrooms = int(input("Enter number of bedrooms: "))

# Prediction
new_house = np.array([[area, bedrooms]])
predicted_price = model.predict(new_house)

print("Predicted House Price:", predicted_price[0])
