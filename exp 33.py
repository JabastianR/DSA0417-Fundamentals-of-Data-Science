import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Example dataset
data = {
    'engine_size': [1.5,2.0,2.5,3.0,1.8,2.2,3.5],
    'horsepower': [120,150,180,220,140,160,250],
    'fuel_efficiency': [18,15,14,12,17,16,10],
    'price': [20000,25000,30000,38000,23000,27000,45000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['engine_size','horsepower','fuel_efficiency']]
y = df['price']

# Train-Test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train,y_train)

# Prediction
y_pred = model.predict(X_test)

# Model evaluation
mse = mean_squared_error(y_test,y_pred)
r2 = r2_score(y_test,y_pred)

print("Mean Squared Error:",mse)
print("R2 Score:",r2)

# Feature importance (coefficients)
importance = pd.Series(model.coef_, index=X.columns)
print("\nFeature Influence on Price:")
print(importance)
