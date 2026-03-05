import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 180, 170, 200, 220, 210]

# 1. Line Plot - Sales Trend
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 2. Scatter Plot - Sales
plt.figure()
plt.scatter(months, sales)
plt.title("Monthly Sales Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# 3. Bar Plot - Sales
plt.figure()
plt.bar(months, sales)
plt.title("Monthly Sales Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
