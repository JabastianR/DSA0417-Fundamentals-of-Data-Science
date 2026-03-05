import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
temperature = [22, 24, 28, 32, 35, 33]   # in degree Celsius
rainfall = [10, 15, 20, 40, 80, 120]     # in mm

# 1. Line Plot - Temperature
plt.figure()
plt.plot(months, temperature, marker='o')
plt.title("Monthly Temperature Trend")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()

# 2. Scatter Plot - Rainfall
plt.figure()
plt.scatter(months, rainfall)
plt.title("Monthly Rainfall Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.show()
