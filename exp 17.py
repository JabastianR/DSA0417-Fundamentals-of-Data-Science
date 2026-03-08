import pandas as pd
import matplotlib.pyplot as plt
import string

# Load dataset
data = pd.read_csv(r"C:\Users\cravi\OneDrive\Desktop\Jabastian college\Fundamentals of data science lab\stu.csv")

# Get feedback column
text = " ".join(data["Name"].astype(str))

# Convert to lowercase
text = text.lower()

# Remove punctuation
for p in string.punctuation:
    text = text.replace(p, "")

# Simple stop words list
stop_words = ["the","and","is","in","to","of","for","on","a","an"]

# Remove stop words
words = [word for word in text.split() if word not in stop_words]

# Calculate frequency
freq = pd.Series(words).value_counts()

# User input for top N words
N = int(input("Enter number of top words to display: "))

top_words = freq.head(N)

print("\nTop Words:")
print(top_words)

# Plot bar graph
plt.bar(top_words.index, top_words.values)
plt.title("Top Frequent Words in Feedback")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()
