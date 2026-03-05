# Q13: Word Frequency from sample_text.txt

from collections import Counter

# Read the text file
with open(r"C:\Users\cravi\OneDrive\Desktop\Jabastian college\Fundamentals of data science lab\sample.txt") as file:
    text = file.read()

# Process text
text = text.lower()                     # convert to lowercase
words = text.split()                    # split into words

# Remove punctuation (basic cleaning)
clean_words = [word.strip(".,!?;:()[]") for word in words]

# Calculate frequency
word_frequency = Counter(clean_words)

# Display frequency distribution
print("Word Frequency Distribution:")
for word, count in word_frequency.items():
    print(word, ":", count)
