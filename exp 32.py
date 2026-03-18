import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
df = pd.DataFrame({
    'size':[800,1000,1200,1500],
    'price':[150000,200000,240000,300000]
})

# Scatter plot
plt.scatter(df['size'], df['price'])
plt.show()

# Model
X = df[['size']]
y = df['price']

model = LinearRegression()
model.fit(X,y)

# Prediction
pred = model.predict(X)
print("R2 Score:", model.score(X,y))
