# Q14: Age Frequency Distribution

import pandas as pd

# Example DataFrame (remove if your data already exists)
data = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'age': [25, 30, 25, 35, 30, 40]
}

sales_data = pd.DataFrame(data)

# Frequency distribution of ages
age_frequency = sales_data['age'].value_counts().sort_index()

print("Age Frequency Distribution:")
print(age_frequency)
