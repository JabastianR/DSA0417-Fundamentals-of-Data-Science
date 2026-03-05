# Q15: Likes Frequency Distribution

import pandas as pd

# Example dataset
data = {
    'post_id': [101, 102, 103, 104, 105, 106],
    'likes': [10, 25, 10, 50, 25, 10]
}

posts_data = pd.DataFrame(data)

# Frequency distribution of likes
likes_frequency = posts_data['likes'].value_counts().sort_index()

print("Likes Frequency Distribution:")
print(likes_frequency)
