# Q16: Word frequency from customer reviews

from collections import Counter

# Example customer reviews
reviews = [
    "This product is very good",
    "Good quality and good price",
    "This product is excellent",
    "Very good product and quality"
]

# Combine all reviews
text = " ".join(reviews)

# Convert to lowercase and split words
words = text.lower().split()

# Calculate frequency distribution
freq = Counter(words)

print("Word Frequency Distribution:")
for word, count in freq.items():
    print(word, ":", count)
