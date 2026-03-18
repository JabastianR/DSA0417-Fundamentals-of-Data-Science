import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Dataset
df = pd.DataFrame({
    'mileage':[20000,30000,40000],
    'age':[2,3,4],
    'price':[15000,14000,13000]
})

X = df[['mileage','age']]
y = df['price']

model = DecisionTreeRegressor()
model.fit(X,y)

# User input
mileage = int(input("Enter mileage: "))
age = int(input("Enter age: "))

pred = model.predict([[mileage,age]])
print("Predicted Price:", pred[0])
